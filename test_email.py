from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

user_email = 'for.test.simbirsoft@gmail.com'
user_pass = 'gbm-XT8-4VZ-77t'
theme = '«Simbirsoft Тестовое задание»'

driver = webdriver.Firefox()
driver.get("http://gmail.com")

email = driver.find_element_by_id('identifierId')
time.sleep(1)
email.send_keys(user_email)
time.sleep(1)
email.send_keys(Keys.ENTER)

time.sleep(5)

email_pass = driver.find_element_by_name('password')
email_pass.send_keys(user_pass)
time.sleep(1)
email_pass.send_keys(Keys.ENTER)

time.sleep(5)

find_param = driver.find_element_by_name('q')
time.sleep(1)
find_param.send_keys('in:inbox ' + theme)

time.sleep(1)
find_param.send_keys(Keys.ENTER)
time.sleep(2)
num_of_letters = driver.find_elements_by_xpath('//span[@class="ts"]')
time.sleep(2)
# print(num_of_letters)
#//*[@id=":5e"]/span/span[2],
# /html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/span/div[1]/span/span[2]



new_letter_create = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
time.sleep(1)
new_letter_create.click()
time.sleep(2)

send_letter_address = driver.find_element_by_name('to')
time.sleep(1)
send_letter_address.send_keys('for.test.simbirsoft@gmail.com')
time.sleep(1)
send_letter_address.send_keys(Keys.ENTER)
time.sleep(1)
send_letter = driver.find_element_by_name('subjectbox')
time.sleep(1)
send_letter.send_keys(theme)

time.sleep(1)
send_letter_text = driver.find_element_by_xpath('//div[@class="Am Al editable LW-avf tS-tW"]')
time.sleep(2)
send_letter_text.send_keys('Тема письма ' + theme + 'ФИО')
time.sleep(1)
send_letter_text.send_keys(Keys.CONTROL, Keys.ENTER)
driver.quit()
