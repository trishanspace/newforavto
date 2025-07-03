import time
from itertools import product, count
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProdactPage



def test_open_galaxys6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProdactPage(driver)
    product_page = 'Samsung galaxy s6'

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_product_count(2)