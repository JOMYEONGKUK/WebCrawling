# 네이버 'VIEW' 섹션의 내용 수집하기
# 검색 키워드 입력 : 봄 여행
# 파일 저장(txt) : C:\python_temp\data\test_20220222_Ex03.txt

import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

# 검색할 키워드를 입력 하는 부분
search_txt = input("검색할 키워드를 입력해주세요 : ")

server = 'C:\\web_driver\\chromedriver.exe'
driver = webdriver.Chrome(server) # 크롬으로 실행함
driver.get('https://www.naver.com/') # 크롬 브라우저 안에 naver 사이트 실행

#검색창에 키워드를 넣는 부분
element = driver.find_element('id','query') # 검색창에 입력 / 20220710 코드 수정
element.send_keys(search_txt) # search_txt에서 입력 받은 키워드를 넣음
time.sleep(2) # 검색창에 키워드를 입력하는 시간 2초

# 네이버 검색창 우측 돋보기 모양 검색 버튼을 클릭합니다.
element = driver.find_element('id','search_btn').click() # 20220710 코드 수정