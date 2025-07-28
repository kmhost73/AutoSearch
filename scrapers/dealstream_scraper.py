from bs4 import BeautifulSoup

def scrape_dealstream(driver):
    listings = []
    driver.get("https://www.dealstream.com/for-sale")
    soup = BeautifulSoup(driver.page_source, "html.parser")

    for item in soup.select(".listing"):  # Adjust this selector as needed
        title = item.get_text(strip=True)
        listings.append({
            "title": title,
            "source": "DealStream",
            "link": driver.current_url
        })

    return listings
