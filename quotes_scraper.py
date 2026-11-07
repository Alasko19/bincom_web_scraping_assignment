import requests
import pandas as pd
import time

from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Website URL
base_url = "https://quotes.toscrape.com/"

# Creating a session
session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

# Storing unique authors
authors_data = []

# Keeping track of the authors already collected
collected_authors = set()


# Visit pages until we collect 13 distinct authors
for page_number in range(1, 13):

    page_url = urljoin(
        base_url,
        f"page/{page_number}/"
    )

    print(f"\nScraping Quotes Page {page_number}...")

    response = session.get(page_url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    quotes = soup.select(".quote")

    # Stop if there are no more quotes
    if not quotes:
        print("No more quotes found.")
        break

    # Extracting authors from the quote cards
    for quote in quotes:

        author_link = quote.select_one(
            ".author + a"
        )

        if author_link is None:
            continue

        author_url = urljoin(
            page_url,
            author_link["href"]
        )

        # Skipping authors already collected
        if author_url in collected_authors:
            continue

        # Visiting the author's profile page
        author_response = session.get(
            author_url,
            timeout=30
        )

        author_response.raise_for_status()

        author_soup = BeautifulSoup(
            author_response.text,
            "html.parser"
        )

        # Author name
        name_element = author_soup.select_one(
            ".author-title"
        )

        name = (
            name_element.get_text(strip=True)
            if name_element
            else "Unknown"
        )

        # Date of birth
        birth_date_element = author_soup.select_one(
            ".author-born-date"
        )

        date_of_birth = (
            birth_date_element.get_text(strip=True)
            if birth_date_element
            else "Not available"
        )

        # Birthplace
        birthplace_element = author_soup.select_one(
            ".author-born-location"
        )

        birthplace = (
            birthplace_element.get_text(strip=True)
            if birthplace_element
            else "Not available"
        )

        # Author description
        description_element = author_soup.select_one(
            ".author-description"
        )

        description = (
            description_element.get_text(" ", strip=True)
            if description_element
            else "No description available"
        )

        # Saving author information
        authors_data.append({

            "Author Name": name,
            "Nationality": "Not provided by source",
            "Birthplace": birthplace,
            "Date of Birth": date_of_birth,
            "Description": description,
            "Author URL": author_url

        })

        # Marking this author as collected
        collected_authors.add(author_url)

        print(f"Scraped Author: {name}")

        time.sleep(0.2)

        # Stoping after collecting 13 distinct authors
        if len(authors_data) >= 13:
            break

    if len(authors_data) >= 13:
        break


# Converting results into a DataFrame
df = pd.DataFrame(authors_data)


# displaying result
print("AUTHOR SCRAPING COMPLETED")

print("Total distinct authors:", len(df))

print("\nFirst five authors:")
print(df.head())


# results save to CSV
df.to_csv(
    "quotes_authors.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nData successfully saved as quotes_authors.csv")