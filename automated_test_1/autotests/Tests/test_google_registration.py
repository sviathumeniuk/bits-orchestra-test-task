import unittest
from Helpers.webdriver_factory import WebDriverFactory
from Pages.registration_page import RegistrationPage

class TestGoogleRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriverFactory.get_driver()
        self.wait = WebDriverFactory.get_wait(self.driver)
        self.registration_page = RegistrationPage(self.driver, self.wait)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_registration_flow(self):
        """Test the Google account registration flow"""
        self.registration_page.open_registration_page()
        self.registration_page.fill_name_details("Sviat", "Humeniuk")
        self.registration_page.fill_date_of_birth("1", "червень", "2000")
        self.registration_page.select_gender("Чоловік")
        self.registration_page.create_email("sviat.humeniuk123")
        self.registration_page.set_password("Password123!")
        
if __name__ == "__main__":
    unittest.main()