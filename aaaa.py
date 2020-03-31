


from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("lang=ko_KR")
#driver = webdriver.Chrome('C:/Users/chanwoo/Desktop/macro/chromedriver', chrome_options=options)
driver = webdriver.Chrome('/home/ubuntu/chromedriver', chrome_options=options)

driver.get('https://www.naver.com')
driver.implicitly_wait(3)

html = driver.find_element_by_xpath('//*[@id="PM_ID_ct"]/div[1]/div[2]').get_attribute('innerHTML')
soup = bs(html, 'html.parser')
test = soup.find_all('span', href=False)

print(test)
