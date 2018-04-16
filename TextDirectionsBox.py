# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TextDirectionsBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_text_directions_box(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/polls/")
        driver.find_element_by_id("StartPoint").click()
        driver.find_element_by_id("StartPoint").clear()
        driver.find_element_by_id("StartPoint").send_keys("roo")
        driver.find_element_by_xpath("//div[@id='StartPointautocomplete-list']/div").click()
        driver.find_element_by_id("EndPoint").click()
        driver.find_element_by_id("EndPoint").clear()
        driver.find_element_by_id("EndPoint").send_keys("room")
        driver.find_element_by_xpath("//div[@id='EndPointautocomplete-list']/div[3]/strong").click()
        driver.find_element_by_id("findroute").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
