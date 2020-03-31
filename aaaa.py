


from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome('C:/Users/chanwoo/Desktop/macro/chromedriver', chrome_options=options)
#driver = webdriver.Chrome('/home/ubuntu/chromedriver', chrome_options=options)

driver.get('https://ecm.dgist.ac.kr/login.jsp')
driver.implicitly_wait(3)

elem_login = driver.find_element_by_id("username")
elem_login.clear()
elem_login.send_keys("ixora99")

elem_login = driver.find_element_by_id("passwordTest")
elem_login.clear()
elem_login.send_keys("zinnia99####")

driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
driver.find_element_by_xpath('//*[@id="content"]/div/ul/li[2]/a').click()


driver.switch_to_window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

driver.find_element_by_xpath('//*[@id="0021"]/a').click()
driver.find_element_by_xpath('//*[@id="0008"]/a').click()

driver.find_element_by_xpath('//*[@id="boardForm"]/table/tbody/tr[1]/td[2]/a').click()




'''
html = driver.find_element_by_xpath('//*[@id="boardForm"]/table/tbody').get_attribute('innerHTML')
soup = bs(html, 'html.parser')
test = soup.find('a')

print(test.attrs['href'])
'''
