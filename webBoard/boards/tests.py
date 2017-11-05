from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home


class HomeTests(TestCase):

    # Django would return a status code 500 if errors, which means Internal Server Error
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # test if Django returned the correct view function for the requested URL. This is also a useful test because as we progress with the development, you will see that the urls.py module can get very big and complex. The URL conf is all about resolving regex. There are some cases where we have a very permissive URL, so Django can end up returning the wrong view function
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
