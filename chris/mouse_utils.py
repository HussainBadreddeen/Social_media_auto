import time
import random
from selenium.webdriver.common.action_chains import ActionChains

def human_like_mouse_move(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    # Random delay before next action (human-like delay)
    time.sleep(random.uniform(0.5, 1.5))  # Randomized delay to mimic human hesitation

    # Perform a small, random movement to simulate natural behavior
    for _ in range(random.randint(1, 3)):
        x_offset = random.randint(-20, 20)
        y_offset = random.randint(-20, 20)
        actions.move_by_offset(x_offset, y_offset).perform()
        time.sleep(random.uniform(0.2, 0.6))  # Short pauses between movements

    # Slight pause before the final click to mimic hesitation
    time.sleep(random.uniform(0.3, 0.7))

    actions.move_to_element(element).perform()  # Move back to the element if necessary
    time.sleep(random.uniform(0.2, 0.5))  # Random delay before the final click
