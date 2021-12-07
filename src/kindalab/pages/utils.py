from selenium.webdriver.common.by import By


class Page:

    url = None

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.url)

    def get_title(self):
        return

    def open_social_media(self, social):
        self.browser.find_element(By.CSS_SELECTOR, f'a[href*={social}]')


class HomePage(Page):

    url = 'https://kindalab.co/'

    def get_overview(self):
        overview = self.browser.find_element(By.CLASS_NAME, 'overview-container')
        return overview.text


class TeamPage(Page):

    url = 'https://www.google.com/'
