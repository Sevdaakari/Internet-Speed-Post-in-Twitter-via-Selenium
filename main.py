from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

PROMISED_DOWN = 200
PROMISED_UP = 200
CHROME_DRIVER_PATH = r"my-path-to-driver/chromedriver.exe"
TWITTER_EMAIL = "myemail@mail.com"
TWITTER_PASSWORD = "mypassword"


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        URL = 'https://www.speedtest.net/'
        self.driver.get(URL)
        time.sleep(1)
        accept = self.driver.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler')
        accept.click()
        time.sleep(1)
        go = self.driver.find_element(By.CLASS_NAME, 'js-start-test.test-mode-multi')
        go.click()
        time.sleep(30)
        down_speed = self.driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed")
        if down_speed.text != "—":
            result_down = down_speed.text
            print(result_down)
            result_down = self.down
        time.sleep(40)
        up_speed = self.driver.find_element(By.CLASS_NAME, 'result-data-large.number.result-data-value.upload-speed')
        if up_speed.text != '—':
            result_up = up_speed.text
            print(result_up)
            result_up = self.up

    def login(self):
        time.sleep(3)
        self.driver.get(url=r'https://twitter.com/i/flow/login')
        time.sleep(2)
        sign_in = self.driver.find_element(By.NAME, "text")
        sign_in.click()
        sign_in.send_keys(TWITTER_EMAIL)
        sign_in.send_keys(Keys.ENTER)
        time.sleep(1)
        try:
            user_name = self.driver.find_element(By.NAME, "text")
            user_name.click()
            user_name.send_keys("myname")
            user_name.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.NAME, 'password')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
        except Exception:
            password = self.driver.find_element(By.NAME, 'password')
            time.sleep(1)
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)

    def twit_post(self):
        time.sleep(3)
        twit = self.driver.find_element(By.CSS_SELECTOR, value='.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        twit.click()
        twit_text = f"This is a test twit!\nDear provider, my internet speed is: Download {self.down} and Upload {self.up}."
        twit.send_keys(twit_text)
        twit.send_keys(Keys.ENTER)
        time.sleep(3)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        post.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
time.sleep(5)
if PROMISED_UP > bot.up and PROMISED_DOWN > bot.down:
    bot.login()
    bot.twit_post()

