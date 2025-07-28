from bs4 import BeautifulSoup

def scrape_websiteclosers(driver):
    listings = []
    driver.get("https://www.websiteclosers.com/buy-websites-for-sale")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.select(".listing-title"):
        title = item.get_text(strip=True)
        listings.append({
            "title": title,
            "source": "WebsiteClosers",
            "link": driver.current_url
        })
    return listings