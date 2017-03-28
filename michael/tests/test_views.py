from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from michael.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn("Michael Hunter's Homepage", html)
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_displays_correct_name(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn("<h1>Michael Hunter</h1>", html)


