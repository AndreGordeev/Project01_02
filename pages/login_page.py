import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://qatest-dev.indvp.com/'
    login_user = 'andregrdv@gmail.com'
    password = '1234qwerty_'



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    sign_in_button ='//button[@class="Header-Button Header-Button_type_account Header-Button_likeLink"]'
    user_name = '//input[@id="email"]'
    password_locator = '//input[@id="password"]'
    login_button = '//button[@class="Button"]'
    dash_board_button = '//button[@class="ExpandableContent-Button MyAccountTabList-ExpandableContentButton"]'

    #Getters

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dash_board_button)))


    #Actions
    def click_sign_in_button(self):
        self.get_sign_in_button().click()
        print("click sign in button")
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")
    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")
    def click_login_button(self):
        self.get_login_button().click()
        print("click login button")


    # Methods
    def authorisation(self):
        Logger.add_start_step(method = 'authorisation')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_sign_in_button()
        self.input_user_name('andregrdv@gmail.com')
        self.input_password('1234qwerty_')
        self.click_login_button()
        time.sleep(5)
        self.get_current_url()
        self.assert_url('https://qatest-dev.indvp.com/my-account/dashboard')
        Logger.add_end_step(url= self.driver.current_url, method = 'authorisation')