# main.py

import logging
import os
import sys
from datetime import datetime
from utils.google_sheets import push_to_google_sheets
from scrapers.bizbuysell_scraper import scrape_bizbuysell
from scrapers.businessbroker_scraper import scrape_businessbroker
from scrapers.businessesforsale_scraper import scrape_businessesforsale
from scrapers.dealstream_scraper import scrape_dealstream
from scrapers.globalbx_scraper import scrape_globalbx
from scrapers.bizquest_scraper import scrape_bizquest
from scrapers.websiteclosers_scraper import scrape_websiteclosers
from scrapers.mergernetwork_scraper import scrape_mergernetwork
from scrapers.equisource_scraper import scrape_equisource
from scrapers.raincatcher_scraper import scrape_raincatcher
from scrapers.quietlight_scraper import scrape_quietlight
from utils.selenium_driver import get_stealth_driver

# Set up logging to both file and console
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"autoscraper_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='a', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

print(f"📝 Log file: {log_file}")

def main():
    try:
        logging.info("Running AutoSearch export to Google Sheets")

        # Initialize a stealth Selenium driver for scrapers that need it
        driver = get_stealth_driver()

        # Collect listings from all scrapers
        listings = []
        listings += scrape_bizbuysell()
        listings += scrape_businessbroker()
        listings += scrape_businessesforsale()
        listings += scrape_dealstream(driver)
        listings += scrape_globalbx(driver)
        listings += scrape_bizquest(driver)
        listings += scrape_websiteclosers(driver)
        listings += scrape_mergernetwork(driver)
        listings += scrape_equisource(driver)
        listings += scrape_raincatcher(driver)
        listings += scrape_quietlight(driver)

        driver.quit()

        if listings:
            msg = f"Found {len(listings)} listings. Uploading to Google Sheets..."
            print(msg)
            logging.info(msg)
            push_to_google_sheets(listings)
            print("✅ Listings pushed to Google Sheets successfully.")
            logging.info("✅ Listings pushed to Google Sheets successfully.")
        else:
            msg = "⚠️ No listings found from any source."
            print(msg)
            logging.warning(msg)

    except Exception as e:
        error_msg = f"❌ Failed to push data to Google Sheets: {e}"
        logging.error(error_msg)
        print(error_msg)

if __name__ == "__main__":
    main()
