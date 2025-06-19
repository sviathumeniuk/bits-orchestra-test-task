from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    DAY_FIELD = (By.ID, "day")
    MONTH_DROPDOWN = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
    GENDER_DROPDOWN = (By.ID, "gender")
    CREATE_EMAIL_OPTION = (By.XPATH, "//div[contains(text(),'Створити власну адресу Gmail')]")
    USERNAME_FIELD = (By.NAME, "Username")
    PASSWORD_FIELD = (By.NAME, "Passwd")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "PasswdAgain")
    NEXT_BUTTON = (By.XPATH, "//span[text()='Далі']/parent::button")
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
    def open_registration_page(self):
        self.driver.get("https://accounts.google.com/signup")
        return self
    
    def fill_name_details(self, first_name, last_name):
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_FIELD)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.click_next_button()
        return self

    def fill_date_of_birth(self, day, month, year):
        self.wait.until(EC.presence_of_element_located(self.DAY_FIELD)).send_keys(day)
        self.driver.find_element(*self.YEAR_FIELD).send_keys(year)

        month_dropdown = self.wait.until(EC.element_to_be_clickable(self.MONTH_DROPDOWN))
        month_dropdown.click()
        month_option = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//span[contains(text(),'{month}')]"
        )))
        self.driver.execute_script("arguments[0].click();", month_option)
        return self

    def select_gender(self, gender):
        gender_dropdown = self.wait.until(EC.element_to_be_clickable(self.GENDER_DROPDOWN))
        gender_dropdown.click()
        gender_option = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//span[contains(text(), '{gender}')]"
        )))
        self.driver.execute_script("arguments[0].click();", gender_option)
        self.click_next_button()
        return self

    def create_email(self, username):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_EMAIL_OPTION)).click()
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.click_next_button()
        return self

    def set_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.click_next_button()
        return self

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()
        return self