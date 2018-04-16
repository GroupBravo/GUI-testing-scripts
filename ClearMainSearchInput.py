# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ClearMainSearchInput(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_clear_main_search_input(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/polls/")
        driver.find_element_by_id("SearchInput").click()
        driver.find_element_by_id("SearchInput").clear()
        driver.find_element_by_id("SearchInput").send_keys("roo")
        driver.find_element_by_xpath("//div[@id='SearchInputautocomplete-list']/div[1]").click()
        driver.find_element_by_id("clearsearch").click()
        # Warning: assertTextNotPresent may require manual changes
        self.assertNotRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*id=SearchInput[\s\S]*$")
    
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
