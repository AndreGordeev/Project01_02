from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys,ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.paiment_page import Paiment_page
from base.base_class  import Base


def test_link_about():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\TOOLS\SeleniumInfo_and_drivers\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print("start test")
    login = Login_page(driver)
    login.authorisation()

    mp = Main_page(driver)
    mp.select_menu()


    print("test success")




