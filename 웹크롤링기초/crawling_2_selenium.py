from selenium import webdriver
#입력하기 위한 import
from selenium.webdriver.common.keys import Keys
#페이지 로딩을 기다리는 데에 사용할 time 모듈
import time
#By 사용을 위한 import
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("C:\crawling\chromedriver.exe",options=options)


driver.get('https://www.google.co.kr')

time.sleep(3)

search = driver.find_element(By.NAME, 'q')

#search 변수에 저장된 곳에 값을 전송
search.send_keys('이화여자대학교 사이버 캠퍼스')
time.sleep(2)

#search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)




