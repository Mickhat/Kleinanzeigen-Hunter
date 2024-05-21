import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Discord Webhook URL (Replace 'your_discord_webhook_url' with your actual Discord webhook URL)
DISCORD_WEBHOOK_URL = 'your_discord_webhook_url'

# Gespeicherte IDs der letzten Anzeigen
posted_ids = set()

def send_to_discord(message):
    data = {
        "content": message
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print('Message successfully sent to Discord')
    else:
        print('Failed to send message to Discord')

def fetch_kleinanzeigen():
    global posted_ids

    # Setup WebDriver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Access the search page
        driver.get("https://www.kleinanzeigen.de/s-berlin/laptop/k0l3331r50")

        time.sleep(5)  # Wait for the page to load

        # Extract ads
        ads = driver.find_elements(By.CLASS_NAME, 'aditem')

        new_ads = []
        for ad in ads:
            try:
                ad_id = ad.get_attribute('data-adid')
                if ad_id not in posted_ids:
                    title_element = ad.find_element(By.CLASS_NAME, 'text-module-begin')
                    title = title_element.text
                    link = title_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    try:
                        price = ad.find_element(By.CLASS_NAME, 'aditem-main--middle--price-shipping--price').text
                    except:
                        price = 'N/A'
                    new_ads.append((ad_id, title, price, link))
                    posted_ids.add(ad_id)
            except Exception as e:
                print(f'Error processing ad: {e}')

        driver.quit()
        return new_ads
    except Exception as e:
        print(f'Error fetching ads: {e}')
        driver.quit()

def main():
    while True:
        new_ads = fetch_kleinanzeigen()
        for ad_id, title, price, link in new_ads:
            message = f"**{title}**\nPreis: {price}\nLink: {link}"
            send_to_discord(message)
        time.sleep(120)

if __name__ == "__main__":
    main()
