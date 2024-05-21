# Kleinanzeigen Discord Notifier

This script fetches the latest listings from Kleinanzeigen.de for a specific search term and posts them to a Discord channel via a webhook.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- Google Chrome browser
- ChromeDriver

## How It Works
- The script initializes a headless Chrome browser using Selenium.
- It navigates to the specified search URL on Kleinanzeigen.de.
- It extracts the listings on the page.
- It checks if the listing has already been posted to Discord by checking a set of posted IDs.
- If the listing is new, it posts the listing details (title, price, and link) to the specified Discord channel via the webhook.
- It waits for 2 minutes and repeats the process.

## Installation

1. **Clone the repository or download the script.**

2. **Install required Python packages:**
    ```sh
    pip install selenium webdriver-manager requests
    ```

3. **Download ChromeDriver:**
    Make sure you have ChromeDriver installed and it matches the version of your installed Chrome browser. You can download it from [here](https://sites.google.com/chromium.org/driver/downloads).

## Setup

1. **Replace the placeholder in the script with your actual Discord webhook URL:**
    ```python
    DISCORD_WEBHOOK_URL = 'your_discord_webhook_url'
    ```

2. **Update the search URL in the script if necessary:**
    ```python
    driver.get("https://www.kleinanzeigen.de/s-berlin/laptop/k0l3331r50")
    ```
