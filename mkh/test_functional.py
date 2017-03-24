from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time
import unittest

class PWFunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_home_page_elements(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Michael Hunter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Michael Hunter', header_text)