import time
import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_factory import create_driver
from pages.movie_page import MoviePage

# 📁 Ensure screenshot directory exists
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture
def driver():
    drv = create_driver()
    yield drv
    drv.quit()

def take_screenshot(driver, name):
    try:
        path = os.path.join(SCREENSHOT_DIR, f"{name}.png")

        # Small delay to allow DOM rendering (optional but helpful)
        time.sleep(1)

        success = driver.save_screenshot(path)
        if success and os.path.getsize(path) > 0:
            print(f"[Screenshot saved] {path}")
        else:
            print(f"[Failed to save screenshot] File may be empty or invalid: {path}")

    except Exception as e:
        print(f"[Exception while saving screenshot] {e}")

# Sort movies and verify last is 'The Phantom Menace'
def test_sort_movies_by_title(driver):
    page = MoviePage(driver)
    page.open_homepage()
    page.sort_by_column("Title", clicks=1)
    time.sleep(2)  # Give time for sorting animation

    page.take_screenshot("sorted_by_title")
    rows = page.get_table_rows()
    last_title = rows[-1].find_element(By.CSS_SELECTOR, "td").text
    assert last_title == "The Phantom Menace"

# View ‘The Empire Strikes Back’ and check if species list has ‘Wookie’
def test_species_has_wookie(driver):
    page = MoviePage(driver)
    page.open_homepage()
    page.click_movie("The Empire Strikes Back")

    # Scroll to "Species" section before screenshot
    page.scroll_to_section("Species")
    page.take_screenshot("empire_species_scrolled")

    species = page.get_items_for_section("Species")
    assert any("wookie" in li.text.lower() for li in species)

# Verify ‘Camino’ is NOT in Planets list of ‘The Phantom Menace’
def test_camino_not_in_phantom_menace(driver):
    page = MoviePage(driver)
    page.open_homepage()
    page.click_movie("The Phantom Menace")

    page.scroll_to_section("Planets")
    page.take_screenshot("phantom_planets_scrolled")

    planets = page.get_items_for_section("Planets")
    assert not any("camino" in p.text.lower() for p in planets)