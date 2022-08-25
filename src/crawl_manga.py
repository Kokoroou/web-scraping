from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def open_browser():
    # Declare browser
    browser_options = Options()
    browser_options.add_argument("--incognito")
    browser_options.add_argument("--headless")  # Uncomment this line to open browser in background
    browser_options.add_experimental_option("detach", True)

    # Open browser
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=browser_options)

    return browser


def open_url(browser, url):
    browser.get(url)


def search_manga(manga_name):
    pass


def get_manga_name(browser):
    path_to_manga = browser.find_element(By.XPATH, "//*[@id='breadcrumbs']/span[2]").text

    manga_name = path_to_manga.lstrip("Trang chủ > ")

    return manga_name


def get_chapters_name(browser):
    # Get chapters' name in descending order
    chapters_name = [element.text for element in browser.find_elements(By.CSS_SELECTOR, "a[id^='c_']")]

    return chapters_name


def close_browser(browser):
    browser.close()


if __name__ == "__main__":
    URL = "https://blogtruyen.vn/30710/chainsawman-phan-2"

    # TODO: Make a function return a dictionary of chapters (store name, link,...) from different websites
    # TODO: Make a function show to screen

    chrome = open_browser()
    open_url(chrome, URL)

    manga = get_manga_name(chrome)
    chapters = get_chapters_name(chrome)

    print(f"Chapter mới nhất của {manga} là {chapters[0].lstrip(manga).title()}")

    # Close browser when end process
    close_browser(chrome)
