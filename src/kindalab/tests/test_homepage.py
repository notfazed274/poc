from kindalab.utils import *


class TestHomepage:

    def test_index(self, browser):
        page = HomePage(browser)
        page.open()
        page.open_social_media('facebook')

    def test_another_thing(self, browser):
        page = TeamPage(browser)
        page.open()
        assert 'Google' == browser.title

