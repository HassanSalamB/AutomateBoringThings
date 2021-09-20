from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import unittest


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            "/var/jenkins_home/workspace/PythonGoogleSearch/chromedriver")

    def test_googlesearch(self):
        self.driver.get('https://www.google.com/')
        time.sleep(2)

        q = self.driver.find_element(By.NAME, 'q')

        q.send_keys('webdriver')

        q.submit()
        time.sleep(2)

        print(self.driver.current_url)
        time.sleep(4)

    def exit(self):
        self.driver.close()
