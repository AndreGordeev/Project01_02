from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Client_information_page(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    first_name = '//input[@id="firstname"]'
    last_name = '//input[@id="lastname"]'
    phone_number = '//input[@id= "telephone"]'
    region = '//input[@id= "region_string"]'
    street = '//input[@id= "street"]'
    city = '//input[@id= "city"]'
    postal_code = '//input[@id= "postcode"]'
    #continue_button = '//input[@id= "continue"]'
    # test_word_2 = '//span[@class = "title"]'

    #Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))
    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))


    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))
    # def get_test_word_2(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_word_2)))


    #Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first name")
    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last name")
    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("input postal code")
    def input_street(self, street):
        self.get_street().send_keys(street)
        print("input street")
    def input_region(self, region):
        self.get_region().send_keys(region)
        print("input region")
    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("input phone_number")
    def input_city(self, city):
        self.get_city().send_keys(city)
        print("input region")


    # def click_continue_button(self):
    #     self.get_continue_button().click()
    #     print("continue button clicked")


    # Methods
    def input_info(self):

        Logger.add_start_step(method='ordering')

        self.get_current_url()
        self.input_first_name('Ivan')
        self.input_last_name('Petrov')
        self.input_postal_code('193318')
        self.input_street('Aleksandrov street')
        self.input_phone_number('+3357771122')
        self.input_region('Region')
        self.input_city("City")
        print("bug caught, no opportunity to click finish button")
        #self.click_continue_button()
        Logger.add_end_step(url=self.driver.current_url, method='ordering')


