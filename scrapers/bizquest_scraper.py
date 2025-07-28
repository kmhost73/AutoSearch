from bs4 import BeautifulSoup

def scrape_bizquest(driver):
    listings = []
    driver.get("https://www.bizquest.com/businesses-for-sale-in-tennessee-tn/")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.select(".srTitle"):
        title = item.get_text(strip=True)
        listings.append({
            "title": title,
            "source": "BizQuest",
            "link": driver.current_url
        })
    return listings