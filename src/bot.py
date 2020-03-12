from selenium import webdriver
from time import sleep
email = "email"
password = "password"


class InstaBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.instagram.com')

    def login(self):
        sleep(2)
        email_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        email_in.send_keys(email)

        pw_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        pw_in.send_keys(password)
        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        login_btn.click()
        sleep(5)
        # Exiting the occasional notification popup
        try:
            not_now = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[3]/button[2]')
            not_now.click()
        except:
            print('No popup')


bot = InstaBot()
bot.login()
