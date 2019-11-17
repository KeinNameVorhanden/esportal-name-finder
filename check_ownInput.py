import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Globals
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
options.add_argument('headless')
options.add_argument('window-size=0x0')
path = os.path.dirname(os.path.abspath(__file__))
print(path)
driver = webdriver.Chrome(path + '/chromedriver.exe', options=options)
base_url = 'https://beta.esportal.se/profile/'
url_path = path + '/list.txt'
id = ''


# Opens url
def scan(id):
    driver.get(base_url + id)


# Writes to output
def write_file(id):
    f = open(path + '/output.txt', 'a+')
    f.write(id)
    f.close()


def split_nickname(input, nickname):
    words = input.split(",")
    for i in words:
        scan(i)
        if driver.title == 'Home - Esportal':
            print('free: ' + i)
            i = i + "\n"
            write_file(i)
        else:
            print('used: ' + i)
    return nickname


nickname = ""
input = input("Insert Nickname: ")
split_nickname(input, nickname)
