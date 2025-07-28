from bs4 import BeautifulSoup

def scrape_mergernetwork(driver):
    listings = []
    driver.get("https://www.dealstream.com/for-sale/tennessee-businesses")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.select("h2.title a"):
        title = item.get_text(strip=True)
        link = item.get("href")
        listings.append({
            "title": title,
            "source": "MergerNetwork",
            "link": link if link.startswith("http") else "https://www.dealstream.com" + link
        })
    return listings