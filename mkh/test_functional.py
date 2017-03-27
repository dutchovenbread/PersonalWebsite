from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import sys
import unittest

MAX_WAIT = 10

class PWFunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url=cls.live_server_url

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_home_page_elements(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Michael Hunter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Michael Hunter', header_text)
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:university'))
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:workplace'))


