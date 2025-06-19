from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleRegistrationTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def open_registration_page(self):
        self.driver.get("https://accounts.google.com/signup")
    
    def fill_name_details(self, first_name, last_name):
        self.wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.click_next_button()

    def fill_date_of_birth(self, day, month, year):
        self.wait.until(EC.presence_of_element_located((By.ID, "day"))).send_keys(day)
        self.driver.find_element(By.ID, "year").send_keys(year)

        month_dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, "month")))
        month_dropdown.click()
        month_option = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//span[contains(text(),'{month}')]"
        )))
        self.driver.execute_script("arguments[0].click();", month_option)

    def select_gender(self, gender):
        gender_dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, "gender")))
        gender_dropdown.click()
        gender_option = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//span[contains(text(), '{gender}')]"
        )))
        self.driver.execute_script("arguments[0].click();", gender_option)
        self.click_next_button()

    def create_email(self, username):
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[contains(text(),'Створити власну адресу Gmail')]"
        ))).click()

        self.driver.find_element(By.NAME, "Username").send_keys(username)
        self.click_next_button()

    def set_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.NAME, "Passwd"))).send_keys(password)
        self.driver.find_element(By.NAME, "PasswdAgain").send_keys(password)
        self.click_next_button()

    def click_next_button(self):
        self.driver.find_element(By.XPATH, "//span[text()='Далі']/parent::button").click()

    def close_browser(self):
        self.driver.quit()

    def run_registration(self):
        try:    
            self.open_registration_page()
            self.fill_name_details("Sviat", "Humeniuk")
            self.fill_date_of_birth("1", "червень", "2000")
            self.select_gender("Чоловік")
            self.create_email("sviat.humeniuk123")
            self.set_password("Password123!")
        finally:
            self.close_browser()

if __name__ == "__main__":
    test = GoogleRegistrationTest()
    test.run_registration()