import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from datetime import datetime



class MoviePage:
    URL = "http://localhost:3000"
    def take_screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(filename)
        print(f"[SCREENSHOT SAVED] {filename}")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_homepage(self):
        self.driver.get(self.URL)

    def sort_by_column(self, column_name, clicks=1):
        """
        Click on a table column header to sort the movies.

        :param column_name: e.g., "Title", "Episode", or "Director"
        :param clicks: how many times to click (1 = ascending, 2 = descending)
        """
        # Find the column header by its text
        header_xpath = f"//th[contains(., '{column_name}')]"
        header = self.wait.until(EC.element_to_be_clickable((By.XPATH, header_xpath)))

        for _ in range(clicks):
            header.click()
            time.sleep(1)  # small pause to allow DOM update

    def get_table_rows(self):
        """
        Return all movie rows as a list of WebElements from the homepage movie table.
        """
        tbody_xpath = "//table/tbody"
        tbody = self.wait.until(EC.presence_of_element_located((By.XPATH, tbody_xpath)))
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        return rows

    def click_movie(self, title):
        link_xpath = f"//a[contains(text(), '{title}')]"
        movie_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, link_xpath)))
        movie_link.click()

        # TEMP: wait + show URL and page source for debugging
        #time.sleep(3)
        #print("URL after click:", self.driver.current_url)
        #print("[DEBUG] Page HTML after clicking movie:")
        #print(self.driver.page_source)

    def scroll_to_section(self, section_title):
        section_xpath = f"//h1[contains(text(), '{section_title}')]"
        section_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, section_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_element)
        time.sleep(1)  # Optional: let the animation complete

    def get_items_for_section(self, section_title):
        try:
            # Wait for the section header
            header_xpath = f"//h1[contains(text(),'{section_title}')]"
            header = self.wait.until(EC.visibility_of_element_located((By.XPATH, header_xpath)))

            # Get the first <ul> following the header
            list_xpath = f"{header_xpath}/following::ul[1]"
            ul = self.wait.until(EC.presence_of_element_located((By.XPATH, list_xpath)))

            # Extract all <li> items inside that <ul>
            items = ul.find_elements(By.TAG_NAME, "li")

            print(f"\n[INFO] Section '{section_title}' found with {len(items)} items:")
            for li in items:
                print("-", li.text)

            return items

        except TimeoutException as e:
            print(f"[ERROR] Could not locate section '{section_title}': {e}")
            return []
