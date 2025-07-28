from bs4 import BeautifulSoup

def scrape_raincatcher(driver):
    listings = []
    driver.get("https://raincatcher.com/businesses-for-sale/")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.select(".teaser__title"):
        title = item.get_text(strip=True)
        listings.append({
            "title": title,
            "source": "Raincatcher",
            "link": driver.current_url
        })
    return listings