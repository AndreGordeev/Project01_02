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

    select_bed_and_bath_locator = '/html/body/div[1]/header/div[2]/ul/li[5]/div/figure/figcaption'
    sort_by_button ='/html/body/div/main/section/div/div[1]/div/div/div/div/ul'
    sort_low_to_high = '/html/body/div/main/section/div/div[1]/div/div/div/div/ul/li[3]'
    product_1_locator = '/html/body/div/main/section/div/div[2]/div/ul/li[2]/a/div/p[1]'
    add_product_to_cart_locator_1 = '/html/body/div[1]/main/div/section/div/div[2]/article/div[2]/ul/li/div[3]/div/button[1]'
    # add_product_to_cart_locator_2 = '/html/body/div[1]/main/div/section/div/div[2]/article/div[2]/ul/li[5]/div[3]/div/button[1]/span'
    add_to_cart_button = '/html/body/div[1]/main/div/section/div/div[2]/article/div[1]/button'
    cart = '/html/body/div[1]/header/nav/div[3]/button'
    go_to_cart = '/html/body/div/header/nav/div[3]/div/div/a[1]'


    #Getters
    def get_select_bed_and_bath_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_bed_and_bath_locator)))

    def get_sort_by_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_button)))
    def get_sort_low_to_high(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_low_to_high)))

    def get_product_1_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_locator)))

    def get_add_product_to_cart_locator_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_to_cart_locator_1)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    #Actions
    def click_select_bed_and_bath_locator(self):
        self.get_select_bed_and_bath_locator().click()
        print("bed and bath selected")

    def click_sort_by_button(self):
        self.get_sort_by_button().click()
        print("sort_by_button selected")
    def click_sort_low_to_high(self):
        self.get_sort_low_to_high().click()
        print("sort low to high selected")

    def click_product_1_locator(self):
        self.get_product_1_locator().click()
        print("product_selected")

    def click_add_product_to_cart_locator_1(self):
        self.get_add_product_to_cart_locator_1().click()
        print("product_1 added")


    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("add-to_cart_button pushed")
    def click_cart(self):
        self.get_cart().click()
        print("click cart")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("click go to cart")

    # Methods
    def select_product_1(self):


        Logger.add_start_step(method='select_product_1')
        self.get_current_url()
        self.click_select_bed_and_bath_locator()
        self.click_sort_by_button()
        self.click_sort_low_to_high()
        self.click_product_1_locator()
        self.click_add_product_to_cart_locator_1()
        self.click_add_product_to_cart_locator_1()
        self.click_add_to_cart_button()
        self.click_cart()
        self.click_go_to_cart()
        self.assert_url('https://qatest-dev.indvp.com/cart')
        print('A bug caught, a mistake on page')
        Logger.add_end_step(url=self.driver.current_url, method='select_product_1')



