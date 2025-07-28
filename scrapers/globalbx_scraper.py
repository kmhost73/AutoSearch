from bs4 import BeautifulSoup

def scrape_globalbx(driver):
    listings = []
    driver.get("https://www.globalbx.com/listings/tennessee-businesses-for-sale/")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.select(".listing"):
        title = item.get_text(strip=True)
        listings.append({
            "title": title,
            "source": "GlobalBX",
            "link": driver.current_url
        })
    return listings