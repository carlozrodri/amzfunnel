from httpcore import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amzfunnel.settings')
django.setup()
from core.models import Items, Categorias, Email, ContactUs, Urls
from django.utils.text import slugify

def generate_affiliate_link(original_url, associate_id):
    # Extract the ASIN from the original URL
    asin = original_url.split('/dp/')[1].split('/')[0]
    
    # Build the affiliate link
    affiliate_link = f"https://www.amazon.co.uk/dp/{asin}?tag={associate_id}"
    return affiliate_link

MAX_LENGTH = 100
def truncate_text(text, length=MAX_LENGTH):
    """ Truncate text to the specified length if it exceeds it. """
    return text[:length]

class Scraper:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")  # Activate headless mode
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def scrape_data(self, url):
        try:
            # Open the webpage
            self.driver.get(url)

            # Extract the information using WebDriverWait for better reliability
            titulo_raw = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'productTitle'))).text
            texto_raw1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#feature-bullets > ul > li:nth-child(1) > span'))).text
            texto_raw2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#feature-bullets > ul > li:nth-child(2) > span'))).text
            texto_raw3 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#feature-bullets > ul > li:nth-child(3) > span'))).text
            texto_raw4 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#feature-bullets > ul > li:nth-child(4) > span'))).text
            image = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#imgTagWrapperId > img'))).get_attribute('src')
            category = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#productDetails_detailBullets_sections1 > tbody > tr:nth-child(3) > td > span > span:nth-child(1)'))).text
            category2 = category.split('in ')[1].split(' (')[0]
            print("Title:", titulo_raw[:50], "Description:", "Category:", category2)
            # Generate the affiliate link
            generated_link = generate_affiliate_link(url, 'top8uk0e-21')
            print("Generated affiliate link:", generated_link)
            category_slug = slugify(category2)
            # Create a new instance of AmazonItem model and save it to the database
            category_instance, created = Categorias.objects.get_or_create(
                title=category2,
                defaults={'slug': category_slug}  # Use defaults to ensure the slug is set when creating a new instance
            )
            titulo_raw = truncate_text(titulo_raw)
            texto_raw1 = truncate_text(texto_raw1)
            texto_raw2 = truncate_text(texto_raw2)
            item_description = truncate_text(texto_raw1 + texto_raw2)

            new_item = Items.objects.create(
                title=titulo_raw,
                item_pictures=image,
                item_description=item_description,
                url_amazon=generated_link,
                is_especial=False,    # You need to adjust this based on where the image URL is located on the page
                category=category_instance,
                
            )
            new_item.save()
        # Create the Urls instance without assigning the ManyToManyField directly
            updated_url, created = Urls.objects.update_or_create(
                url=generated_link,  # This assumes 'url' is unique; adjust accordingly
                defaults={
                    'scraped': True,
                    'product_name': titulo_raw,
                    'product_description': item_description,
                    'product_image': image,
                }
            )

            # Use add() or set() to associate the category with the Urls instance
            updated_url.product_category.set([category_instance])  # You can also use add(category_instance)

            print(f"Data {'created' if created else 'updated'} successfully for URL:", titulo_raw)

            print("Data saved successfully for URL:", titulo_raw)

        except TimeoutException as e:
            print("Timeout occurred for URL:", url, "- Couldn't find the required elements:", e)

        except Exception as e:
            print("An error occurred for URL:", url, "-", e)

    def scrape_all_urls(self):
        # Fetch all URL objects where scraped is False
        urls = Urls.objects.filter(scraped=False)

        # Iterate over each URL object and scrape its data
        for url_obj in urls:
            print("Scraping data for:", url_obj.url)
            self.scrape_data(url_obj.url)
    def close_driver(self):
        # Close the webdriver
        self.driver.quit()

# Example usage:
scraper = Scraper()
# scraper.scrape_all_urls()  # Now this will scrape data for all URLs in the database
scraper.close_driver()
