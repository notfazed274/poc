from kindalab.pages.utils import *


class TestHomepage:

    def test_social_media(self, browser):
        page = HomePage(browser)
        page.open()
        page.open_social_media('instagram')

    def test_overview(self, browser):
        page = HomePage(browser)
        page.open()
        phrase = 'We are a team with over'
        overview = page.get_overview()
        assert phrase in overview




