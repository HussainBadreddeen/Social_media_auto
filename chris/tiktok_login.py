import os
import time
from dotenv import load_dotenv
from browser_utils import setup_browser
from login_handler import login_with_cookies_or_prompt

# Load credentials (if needed for fallback email/password login — not used here now)
load_dotenv()
USERNAME = os.getenv("tiktok1_email")  # Used as cookie filename (optional)

# Setup browser with stealth options
driver = setup_browser()

# Try cookie-based login, fallback to manual if needed
if login_with_cookies_or_prompt(driver, username=USERNAME):
    print("[*] Logged in successfully. Ready to perform actions.")
else:
    print("[!] Login failed. Exiting.")
    driver.quit()
    exit()

# Keep browser open for inspection (or do next steps here)
time.sleep(30)
driver.quit()
