Python Web Scraping Projects

Project Overview

This repository contains three Python web scraping projects developed as part of a web scraping assignment.

The projects demonstrate how to extract structured information from websites using Python, Requests, BeautifulSoup, and Pandas.

Projects

1. Books to Scrape

Scrapes the first five catalogue pages from Books to Scrape⁠￼, collecting 100 books.

Information extracted:

* Book name
* Price
* Stock status
* Rating
* Description
* Category
* Product information
* Product URL

Output: data/books_data.csv

2. Quotes to Scrape

Scrapes information about 13 distinct authors from Quotes to Scrape⁠￼.

Information extracted:

* Author name
* Birthplace
* Date of birth
* Description
* Author profile URL

Note: Nationality is not provided by the source website and is therefore recorded as “Not provided by source”.

Output: data/quotes_authors.csv

3. Random Wikipedia Article Scraper

Visits Wikipedia’s random article page and extracts information from the randomly selected article.

Information extracted:

* Article title
* Article URL
* Article text

Output: data/wikipedia_random_article.csv

Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* Visual Studio Code

Project Structure
bincom_web_scraping_assignment/
│
|
│--books_data.csv
|── quotes_authors.csv
│── wikipedia_random_article.csv
│
├── books_scraper.py
├── quotes_scraper.py
├── wikipedia_scraper.py
├── requirements.txt
├── README.md
└── .gitignore

Installation and Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate into the project folder

cd bincom_web_scraping_assignment

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:
.\venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

Running the Scrapers

Run each scraper independently:
Books scraper:

python books_scraper.py

Quotes scraper:

python quotes_scraper.py

Wikipedia scraper:

python wikipedia_scraper.py

The CSV output files are saved in the data/ directory when the output paths are configured accordingly.

Learning Objectives

This project demonstrates practical experience with:

* Sending HTTP requests using Requests.
* Parsing HTML using BeautifulSoup.
* Extracting structured website information.
* Navigating multiple website pages.
* Collecting data from individual product and author pages.
* Working with Pandas DataFrames.
* Exporting scraped information to CSV files.
* Handling randomly selected Wikipedia articles.

Author

Alaba Christian Sunday

Python Developer in Training

GitHub: Alasko19⁠￼

LinkedIn: Sunday⁠￼Alaba Christian 
