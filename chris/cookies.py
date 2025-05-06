# cookies.py
import os
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def get_cookie_filepath(username=None):
    name = username if username else "default"
    # Randomize the cookie filename slightly to avoid detection
    suffix = random.choice(['', str(random.randint(1, 1000))])
    return f"cookies_{name}{suffix}.pkl"


def save_cookies(driver, username=None):
    filepath = get_cookie_filepath(username)
    cookies = driver.get_cookies()
    with open(filepath, "wb") as f:
        pickle.dump(cookies, f)
    print(f"[+] Cookies saved to {filepath}")

def load_cookies(driver, username=None):
    filepath = get_cookie_filepath(username)
    if not os.path.exists(filepath):
        print(f"[!] No cookie file found at {filepath}")
        return False

    driver.get("https://www.tiktok.com/")
    with open(filepath, "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            # Handle sameSite=None bug
            if 'sameSite' in cookie and cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                cookie['sameSite'] = 'Lax'
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"[!] Error adding cookie: {e}")
    driver.refresh()
    return is_logged_in(driver)

def is_logged_in(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@data-e2e, 'top-login-container')]//img"))
        )
        print("[+] Login detected via cookies.")
        return True
    except:
        print("[!] Not logged in after cookie injection.")
        return False
