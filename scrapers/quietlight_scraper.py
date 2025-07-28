from bs4 import BeautifulSoup

def scrape_quietlight(driver):
    listings = []
    driver.get("https://quietlight.com/listings/")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.select("h4.card-title"):
        title = item.get_text(strip=True)
        listings.append({
            "title": title,
            "source": "QuietLight",
            "link": driver.current_url
        })
    return listings