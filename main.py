import time
import sys
from selenium import webdriver

# Globals
driver = webdriver.Chrome('.\chromedriver.exe')
base_url = 'https://beta.esportal.se/profile/'
url_path = '.\list.txt'
id = ''

# Opens url
def scan(id):
    driver.get(base_url + id)
    time.sleep(.10) # currently works, might increase delay in the future.

# Writes to output
def write_file(id):
    f = open('.\output.txt', 'a')
    f.write(id)
    f.close

# Read file and opens url
with open(url_path, 'r') as fp:
    for line in fp:
        id = line
        scan(id)
        if driver.title == 'Home - Esportal':
            print('free: {0}'.format(id.strip('\n')))
            write_file(id)

# Exit when complete
fp.close
driver.close()
sys.exit(0)
