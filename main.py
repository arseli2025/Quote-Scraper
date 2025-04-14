import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful

if response.status_code == 200: 
    print("Successfully accessed the website!")
 #200 status code means that the response was successful.   
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all quote containers (each quote is inside a div with class "quote")
    quotes = soup.find_all('div', class_='quote')
    
    # Loop through each quote and extract the text
    for idx, quote in enumerate(quotes, start=1):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        
        print(f"Quote #{idx}:")
        print(f"Text: {text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(tags)}")
        print("-" * 40)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
