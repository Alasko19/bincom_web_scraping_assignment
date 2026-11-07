import requests
from bs4 import BeautifulSoup


# website url
url = "https://books.toscrape.com/catalogue/page-1.html"

# browser-like request headers

headers = {
    "User-Agent": "Mozilla/5.0"
}

# sending request to the website
response = requests.get(
    url,
    headers=headers,
    timeout=30
)

# checking if the request was successful
print("Status Code:", response.status_code)

# converting the HTML into a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Displaying the page title
print("Website Title:", soup.title.text.strip())

# count the books on the page
books = soup.select("article.product_pod")

print("Number of Books Found:", len(books))

# storing extracted information
