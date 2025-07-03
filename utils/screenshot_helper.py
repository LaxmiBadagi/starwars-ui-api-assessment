import os
import time

SCREENSHOT_DIR = os.path.abspath("screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(driver, name_prefix):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{name_prefix}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    try:
        driver.save_screenshot(filepath)
        print(f"[Screenshot saved] {filepath}")
        return filepath
    except Exception as e:
        print(f"[Failed to save screenshot] {e}")
        return None
