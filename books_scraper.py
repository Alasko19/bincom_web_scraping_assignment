import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Website URL
base_url = "https://books.toscrape.com/"
page_url = urljoin(base_url, "catalogue/page-1.html")

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send request to catalogue page
response = requests.get(
    page_url,
    headers=headers,
    timeout=30
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find all book listings
books = soup.select("article.product_pod")

print("Number of Books Found:", len(books))

books_data = []

# Visit each individual book page
for book in books:

    # Extract book name
    name = book.h3.a["title"]

    # Extract price
    price = book.select_one(".price_color").text.strip()

    # Extract stock status
    stock = book.select_one(".availability").text.strip()

    # Extract rating
    rating = book.select_one(".star-rating")["class"][1]

    # Extract individual book URL
    book_link = book.h3.a["href"]

    # Construct complete book URL
    product_url = urljoin(page_url, book_link)

    # Request individual product page
    product_response = requests.get(
        product_url,
        headers=headers,
        timeout=30
    )

    product_response.raise_for_status()

    product_soup = BeautifulSoup(
        product_response.text,
        "html.parser"
    )

    # Extract book description
    description_element = product_soup.select_one(
        "#product_description + p"
    )

    if description_element:
        description = description_element.text.strip()
    else:
        description = "No description available"

    # Extract category
    category_element = product_soup.select(
        ".breadcrumb li a"
    )

    category = (
        category_element[-1].text.strip()
        if category_element
        else "Unknown"
    )

    # Extract product information table
    product_information = {}

    table_rows = product_soup.select(
        "table.table-striped tr"
    )

    for row in table_rows:

        key = row.th.text.strip()
        value = row.td.text.strip()

        product_information[key] = value

    # Save all extracted information
    books_data.append({
        "Book Name": name,
        "Price": price,
        "Stock Status": stock,
        "Rating": rating,
        "Description": description,
        "Category": category,
        "Product Information": product_information,
        "Product URL": product_url
    })

    print(f"Scraped: {name}")

print("\nTotal Books Scraped:", len(books_data))

# Display the first book's complete information
print("\nFirst Book Details:")
print(books_data[0])


