import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time

import requests
from bs4 import BeautifulSoup
import re


class InstagramBot:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        time.sleep(2)
        user_name_elem = driver.find_element_by_name('username')
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_name('password')
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def get_photo(self, hashtag: str):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)
        for i in range(3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(4)

    def scrape(self) -> str:
        driver = self.driver
        html = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'html5lib')
        return soup

    def get_imgs(self, soup: str) -> list:
        srcs = []
        soup = soup
        imgs = soup.find_all('img')
        for img in imgs:
            if re.search('https', img['src']):
                srcs.append(img['src'])
        return srcs

    def quit_driver(self):
        driver = self.driver
        driver.quit()


def preserve_img(srcs: list):
    srcs = srcs
    num = 1
    for src in srcs:
        time.sleep(10)
        print('get url')
        response = requests.get(src)
        src_content = response.content
        try:
            with open('instagram' + str(num) + '.jpg', 'wb') as bf:
                print('success!')
                bf.write(src_content)
            num += 1
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    hashtag = sys.argv[1]
    instagram = InstagramBot(os.environ.get('INSTAGRAM_USER'), os.environ.get('INSTAGRAM_PASS'))
    instagram.login()
    instagram.get_photo(hashtag)
    soup = instagram.scrape()
    #print(soup)
    srcs = instagram.get_imgs(soup)
    preserve_img(srcs)
    instagram.quit_driver()

