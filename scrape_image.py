
from bs4 import BeautifulSoup
from splinter import Browser
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scrape_image(recipe_id):
    browser = init_browser()
    website_url = f"https://www.food.com/recipe-{recipe_id}"
    browser.visit(website_url)
    website_html = browser.html
    website_soup = BeautifulSoup(website_html, "html.parser")
    website_results = website_soup.find("div", class_="inner-wrapper")
    picture_url = website_results.img["data-src"]
    browser.quit()
    print(picture_url)
    return picture_url

# scrape_image(39087)