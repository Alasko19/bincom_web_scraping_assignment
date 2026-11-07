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
books_data = []

# Extracting details from each book
for book in books:

    name = book.h3.a["title"]

    price = book.select_one(".price_color").text.strip()

    stock = book.select_one(".availability").text.strip()

    rating_element = book.select_one(".star-rating")
    rating = rating_element["class"][1]

    books_data.append({
        "Book Name": name,
        "Price": price,
        "Stock Status": stock,
        "Rating": rating
    })

# displaying extracted information
for book in books_data:
    print(book)


