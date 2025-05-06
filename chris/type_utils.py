import time
import random

def human_like_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.07, 0.2))  # Random delay between keystrokes
        # Random pause before typing the next character
        time.sleep(random.uniform(0.1, 0.3))
