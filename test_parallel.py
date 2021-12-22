import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestParallel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver.maximize_window()

    def test_four(self):
        driver = self.driver
        driver.get("https://www.google.org")

    def test_five(self):
        driver = self.driver
        driver.get("https://www.facebook.com")

    def test_six1(self):
        driver = self.driver
        driver.get("https://www.gmail.com")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()