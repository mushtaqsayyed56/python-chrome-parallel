import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver.maximize_window()


    def test_one(self):
        driver = self.driver
        driver.get("https://www.google.com")
        

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()