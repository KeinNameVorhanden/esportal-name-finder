import sys
import os
from selenium import webdriver

# Globals
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
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


# Read file and opens url
with open(url_path, 'r+') as fp:
    for line in fp:
        id = line
        scan(id)
        if driver.title == 'Home - Esportal':
            print('free: {0}'.format(id.strip('\n')))
            write_file(id)


# Exit when complete
fp.close()
driver.close()
sys.exit(0)
