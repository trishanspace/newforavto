from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxys6 = self.driver.find_element(By.XPATH, '//a[text() = "Samsung galaxy s6"]')
        galaxys6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_product_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count