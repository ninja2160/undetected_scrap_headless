import cloudscraper

# Create a cloudscraper session
scraper = cloudscraper.create_scraper()

# Use the scraper to make a request
url = "https://dexscreener.com/"  # Replace with the URL you want to scrape
response = scraper.get(url)

# Check the response content
print(response.text)  # This will print the HTML content of the page