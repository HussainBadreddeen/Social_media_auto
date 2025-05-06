import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random

def setup_browser():
    options = Options()

    # Random User-Agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    ]
    options.add_argument(f'--user-agent="{random.choice(user_agents)}"')

    # Random Language
    languages = ["en-US", "en", "en-GB", "de-DE"]
    options.add_argument(f"--lang={random.choice(languages)}")

    # Random Window Size
    window_width = random.randint(1200, 1920)
    window_height = random.randint(800, 1080)
    options.add_argument(f"--window-size={window_width},{window_height}")

    # Stealth mode settings
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Disable sandboxing to avoid Linux errors
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options)
    return driver
