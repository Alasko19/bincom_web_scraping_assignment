import requests
import pandas as pd
import json
import time

from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Website URL
base_url = "https://books.toscrape.com/"

# Create a session
session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

# Store all scraped books
books_data = []


# Scrape the first 5 catalogue pages
for page_number in range(1, 6):

    page_url = urljoin(
        base_url,
        f"catalogue/page-{page_number}.html"
    )

    print(f"\nScraping Page {page_number}...")

    response = session.get(page_url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    print("Books found on this page:", len(books))


    # Visit each book on the current page
    for book in books:

        # Book name
        name = book.h3.a["title"]

        # Price
        price = book.select_one(
            ".price_color"
        ).get_text(strip=True)

        # Stock status
        stock_text = book.select_one(
            ".availability"
        ).get_text(" ", strip=True)

        stock_status = (
            "In stock"
            if "in stock" in stock_text.lower()
            else "Out of stock"
        )

        # Rating
        rating = book.select_one(
            ".star-rating"
        )["class"][1]

        # Product URL
        book_link = book.h3.a["href"]

        product_url = urljoin(
            page_url,
            book_link
        )

        # Visit individual book page
        product_response = session.get(
            product_url,
            timeout=30
        )

        product_response.raise_for_status()

        product_soup = BeautifulSoup(
            product_response.text,
            "html.parser"
        )

        # Description
        description_element = product_soup.select_one(
            "#product_description + p"
        )

        if description_element:
            description = description_element.get_text(
                strip=True
            )
        else:
            description = "No description available"

        # Category
        category_links = product_soup.select(
            ".breadcrumb li a"
        )

        if category_links:
            category = category_links[-1].get_text(
                strip=True
            )
        else:
            category = "Unknown"

        # Product information
        product_information = {}

        table_rows = product_soup.select(
            "table.table-striped tr"
        )

        for row in table_rows:

            key = row.th.get_text(strip=True)
            value = row.td.get_text(strip=True)

            product_information[key] = value

        # Save book information
        books_data.append({

            "Book Name": name,
            "Price": price,
            "Stock Status": stock_status,
            "Rating": rating,
            "Description": description,
            "Category": category,
            "Product Information": json.dumps(
                product_information,
                ensure_ascii=False
            ),
            "Product URL": product_url

        })

        print(f"Scraped: {name}")

        # Brief pause between product requests
        time.sleep(0.2)


# Convert scraped data into a DataFrame
df = pd.DataFrame(books_data)


# Display results
print("\n************************")
print("BOOK SCRAPING COMPLETED")
print("**************************")

print("Total books scraped:", len(df))

print("\nDataset shape:")
print(df.shape)

print("\nFirst five books:")
print(df.head())


# Count books by category
print("\nBooks per category:")
print(df["Category"].value_counts())


# Export data to CSV
df.to_csv(
    "books_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nData successfully saved as books_data.csv")