from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    # Use --remote-allow-origins if needed: options.add_argument("--remote-allow-origins=*")
    service = Service()  # Assumes chromedriver is on your PATH
    return webdriver.Chrome(service=service, options=options)
