from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    select_product_1_locator = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2_locator = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3_locator= '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//div[@id="shopping_cart_container"]'
    menu = '//button[@id ="react-burger-menu-btn"]'
    menu_about = '//a[@id="about_sidebar_link"]'


    #Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1_locator)))
    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2_locator)))
    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3_locator)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    def get_menu_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_about)))



    #Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("product_1 selected")
    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("product_2 selected")
    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("product_3 selected")
    def click_cart(self):
        self.get_cart().click()
        print("cart entered")

    def click_menu(self):
        self.get_menu().click()
        print("menu opened")
    def click_menu_about(self):
        self.get_menu_about().click()
        print("menu about opened")



    # Methods
    def select_product_1(self):


        Logger.add_start_step(method='select_product_1')
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_1')

    def select_product_2(self):


        Logger.add_start_step(method='select_product_2')
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_2')

    def select_product_3(self):


        Logger.add_start_step(method='select_product_3')
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_3')



    def select_menu(self):


        Logger.add_start_step(method='select_menu')
        self.get_current_url()
        self.click_menu()
        self.click_menu_about()
        self.assert_url("https://saucelabs.com/")
        Logger.add_end_step(url=self.driver.current_url, method='select_menu')


