import os
import time
import random
from dotenv import load_dotenv
from cookies import load_cookies, save_cookies
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mouse_utils import human_like_mouse_move
from type_utils import human_like_typing

load_dotenv()
EMAIL = os.getenv("tiktok1_email")
PASSWORD = os.getenv("tiktok1_pass")

def login_with_cookies_or_prompt(driver, username=None):
    print("[*] Attempting login via cookies...")
    success = load_cookies(driver, username=username)

    if success:
        return True

    print("[!] Cookie login failed — falling back to automated login flow.")

    try:
        # Step 1: Open TikTok login page
        driver.get("https://www.tiktok.com/login")
        print("Opening TikTok login page...")
        time.sleep(random.uniform(3, 5))  # Random delay to mimic human hesitation

        # Step 2: Scroll before interacting
        driver.execute_script("window.scrollBy(0, 300);")  # Randomize scroll positions
        time.sleep(random.uniform(1, 2))

        # Check if we need to switch to email login
        try:
            # First check if we're already in email mode
            email_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='loginContainer']/div[1]/form/div[1]/input"))
            )
            print("Already in email login mode...")
        except:
            # If not in email mode, try to find and click the email login button
            try:
                # Try the "Use email / username" button
                email_login_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='loginContainer']/div/div/div/div[3]/div[2]/div[2]/div"))
                )
                human_like_mouse_move(driver, email_login_btn)
                email_login_btn.click()
                print("Clicked 'Use email / username' option...")
                time.sleep(random.uniform(2, 4))

                # Now click the "Log in with email" option
                email_option = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='loginContainer']/div[1]/form/div[1]/a"))
                )
                human_like_mouse_move(driver, email_option)
                email_option.click()
                print("Clicked 'Log in with email' option...")
            except Exception as e:
                print(f"Error clicking email option: {e}")
                return False
            
            time.sleep(random.uniform(2, 4))

        # Step 3: Scroll again to simulate reading time
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(random.uniform(1, 2))

        # Step 4: Enter Email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loginContainer']/div[1]/form/div[1]/input"))
        )
        human_like_mouse_move(driver, email_input)
        email_input.click()
        print("Typing in email...")
        human_like_typing(email_input, EMAIL)

        # Step 5: Enter Password
        time.sleep(random.uniform(1, 2))
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loginContainer']/div[1]/form/div[2]/div/input"))
        )
        human_like_mouse_move(driver, password_input)
        password_input.click()
        print("Typing in password...")
        human_like_typing(password_input, PASSWORD)

        # Step 6: Click Login
        time.sleep(random.uniform(1, 2))
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        human_like_mouse_move(driver, login_button)
        login_button.click()
        print("Clicked login button...")

        # Step 7: Wait for successful login
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'For You')]"))
        )
        print("[+] Automated login successful.")
        save_cookies(driver, username=username)
        return True

    except Exception as e:
        print(f"[!] Automated login failed or timed out: {e}")
        return False
