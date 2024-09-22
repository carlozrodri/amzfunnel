from celery import shared_task
from .utils.get_amazon_info import Scraper

@shared_task
def scrape_urls_from_db_task():
    scraper = Scraper()
    scraper.scrape_all_urls()
    scraper.close_driver()
    print("Scraping completed")
