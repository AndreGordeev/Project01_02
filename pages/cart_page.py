from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    checkout_button = '/html/body/div/main/section/div/div[2]/article/div/a[1]'
    enter_adress_button = '/html/body/div/main/section/div/div[1]/form/div[1]/div[2]/button'


    #Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    def get_enter_adress_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_adress_button)))



    #Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("checkout button clicked")
    def click_enter_adress_button(self):
        self.get_enter_adress_button().click()
        print("enter adress button clicked")



    # Methods
    def order_product(self):

        Logger.add_start_step(method='order_product')
        self.refresh_page()
        self.get_current_url()
        self.click_checkout_button()
        self.assert_url("https://qatest-dev.indvp.com/checkout")
        self.click_enter_adress_button()
        Logger.add_end_step(url=self.driver.current_url, method='order_product')



