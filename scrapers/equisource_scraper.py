from bs4 import BeautifulSoup

def scrape_equisource(driver):
    listings = []
    driver.get("https://equisource.com/buy-a-business/")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.select(".property-title"):
        title = item.get_text(strip=True)
        listings.append({
            "title": title,
            "source": "Equisource",
            "link": driver.current_url
        })
    return listings