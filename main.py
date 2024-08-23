import sys
from utils.get_amazon_info import Scraper
# from get_amazon_info import scrape_data

def scrape_urls_from_db():
    # Create an instance of Scraper
    scraper = Scraper()

    # Call the scrape_all_urls method to scrape data for all URLs in the database
    scraper.scrape_all_urls()

    # Close the WebDriver
    scraper.close_driver()

def scrape_single_url(url):
    # Create an instance of Scraper
    scraper = Scraper()

    # Call the scrape_data method on the instance
    scraper.scrape_data(url)

json_file = {
    "urls": [
        "https://www.amazon.co.uk/OUPINKE-Mechanical-Automatic-Waterproof-Stainless/dp/B0BKG8SKSB/ref=sr_1_2_sspa?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sprefix=watches%2Caps%2C89&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "https://www.amazon.co.uk/Hugo-Boss-Analogue-Stainless-1513755/dp/B07WVQVDLV/ref=sr_1_5?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sprefix=watches%2Caps%2C89&sr=8-5",
        "https://www.amazon.co.uk/Citizen-NK5010-51X-Automatic-Watch/dp/B0CYKFFX4V/ref=sr_1_7?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sprefix=watches%2Caps%2C89&sr=8-7",
        "https://www.amazon.co.uk/Emporio-Armani-Mens-Watch-AR2434/dp/B002LZUAFM/ref=sr_1_8?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sprefix=watches%2Caps%2C89&sr=8-8",
        "https://www.amazon.co.uk/Maserati-TRAGUARDO-Watch-Chronograph-Quartz/dp/B09BBKNYJR/ref=sr_1_4_sspa?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sprefix=watches%2Caps%2C89&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "https://www.amazon.co.uk/Emporio-Armani-Chronograph-Stainless-AR11362/dp/B09FZT1RWF/ref=sr_1_10_mod_primary_new?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=watches%2Caps%2C89&sr=8-10",
        "https://www.amazon.co.uk/Maserati-Successo-Limited-Chronograph-quartz/dp/B0B4JYTC9C/ref=sr_1_14_sspa?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sprefix=watches%2Caps%2C89&sr=8-14-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1",
        "https://www.amazon.co.uk/Emporio-Armani-AR11338-Watch/dp/B08WJ83YYG/ref=sr_1_11?crid=YJCJSHERF6MC&dib=eyJ2IjoiMSJ9.nQCDM62SxYbAYiWRuRqgnsIDu8Z0XFy1ipTqLCqp3xa_Q60D3LcnzcsPwNfdfSQFdE31NXEw1MMwtTx2ZOs0aZyEXQ6kdLk-ODPsmvhaMz4UoQGJEbaRu5hBx-ZbvTSDsvkYA2GJ1OQmuYxSwAhf1AUUYvbIqbP2k3BkQ1eVeH3rfmqBOWsrIYbJOCMHjnvT3l0pny8i7gL0Old8IhFnc5JE1P8uRMMqLphCEbqSRiZiDUM_Ky8ct7WSXW2G2cUZaEKBt9zMO-EFfIWSI-09T1Ss_dHS9eBlAwgifFr-ytw.l_RAyd9-jwU5JVhUrlgvgcNKB3tfZJQV1APXZNvOBm0&dib_tag=se&keywords=watches&qid=1724450058&refinements=p_36%3A15000-&rnid=197571031&sprefix=watches%2Caps%2C89&sr=8-11"
  ]
}
def main():
    print("Welcome to the Web Scraper!")

    # Ask the user for their choice
    print("Choose an option:")
    print("1. Scrape URLs from the database")
    print("2. Scrape a single URL")
    print("3. Use the json file inside this file ")

    choice = input("Enter your choice (1, 2 or 3): ")

    if choice == "1":
        # Scrape URLs from the database
        scrape_urls_from_db()
    elif choice == "2":
        # Scrape a single URL provided by the user
        url = input("Enter the URL to scrape: ")
        scrape_single_url(url)
    elif choice == "3":
        # Scrape URLs from the json file
        for url in json_file["urls"]:
            scrape_single_url(url)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
