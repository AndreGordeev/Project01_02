import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver


    """ Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    """ Method assert word"""
    def assert_word(self, word, result):
        value_word=word.text
        print(value_word)
        assert value_word == result
        print("good value word")

    """ Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        #now_date=1
        name_screenshot = 'Screenshot'+now_date+'.png'
        print(name_screenshot)
        self.driver.save_screenshot('D:\\EDUC\\stepikQAAuto\\Tasks\\Project01_02\\screen' + name_screenshot)
        print("screenshot saved")

    """ Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("good url")

    def refresh_page(self):
        self.driver.refresh()
