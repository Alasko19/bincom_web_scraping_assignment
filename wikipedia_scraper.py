import requests
import pandas as pd

from bs4 import BeautifulSoup


# Wikipedia random article URL
url = "https://en.wikipedia.org/wiki/Special:Random"

# Setting request headers
headers = {
    "User-Agent": "PythonWebScrapingAssignment/1.0 (educational project)"
}

# Sending request to Wikipedia
response = requests.get(
    url,
    headers=headers,
    timeout=30
)

response.raise_for_status()

# Getting the final article URL after redirection
article_url = response.url

# Parsing the webpage
soup = BeautifulSoup(
    response.text,
    "html.parser"
)


# Extracting article title
title_element = soup.select_one(
    "#firstHeading"
)

title = (
    title_element.get_text(strip=True)
    if title_element
    else "Title not found"
)


# Extracting main article content
content_element = soup.select_one(
    "#mw-content-text .mw-parser-output"
)

paragraphs = []

if content_element:

    # Search for paragraphs inside nested elements too
    for paragraph in content_element.find_all("p"):

        text = paragraph.get_text(
            " ",
            strip=True
        )

        if text:
            paragraphs.append(text)


# Combine paragraphs into one article text
article_text = "\n\n".join(paragraphs)


# Combining paragraphs into one article text
article_text = "\n\n".join(paragraphs)


# Storing extracted information
wikipedia_data = [{

    "Article Title": title,
    "Article URL": article_url,
    "Article Text": article_text

}]


# Convert to DataFrame
df = pd.DataFrame(wikipedia_data)


# Displaying results
print("WIKIPEDIA SCRAPING COMPLETED")

print("\nArticle Title:")
print(title)

print("\nArticle URL:")
print(article_url)

print("\nArticle Text Preview:")
print(article_text[:2000])

print("\nTotal Characters Extracted:")
print(len(article_text))


# Saving results to CSV file
df.to_csv(
    "wikipedia_random_article.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nData successfully saved as wikipedia_random_article.csv")