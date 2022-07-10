# 네이버 '지식백과' 섹션의 내용 수집하기
# 시트 이름 : 지식백과
# 셀 순서 : 제목 - 내용 - 출처 

# 검색 키워드 입력 : 빅데이터
# 파일 저장(txt) : C:\python_temp\data\test_20220222_Ex05.txt.xls

import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

# 분리하고 수집된 데이터를 데이터 프레임으로 만들어서 csv, xls 형식으로 저장
# 출력 결과를 엑셀 표 형태로 만듭니다.
import pandas as pd
import xlwt

# 검색할 키워드를 입력하는 부분
big_txt = input("검색할 키워드 입력 : ")

# 파일 저장 경로를 입력하는 부분
fx_name = input('검색결과를 저장할 파일 경로와 이름을 지정하세요.\n(예: C:\\Python_temp\\data\\text.xls) : ')

server = 'C:\\web_driver\\chromedriver.exe'
driver = webdriver.Chrome(server) # 크롬으로 실행합니다.
driver.get('https://www.naver.com/') # 크롬 브라우저 안에 naver 사이트 실행

# 검색창에 키워드를 입력 하는 부분
element = driver.find_element('id','query') # 20220710 코드 수정
element.send_keys(big_txt) # big_txt에서 입력 받은 키워드를 넣음
time.sleep(2) # 검색창에 키워드를 입력하는 시간 2초 걸림

# 네이버 검색창 우측 돋보기 모양 검색 버튼을 클릭합니다.
element = driver.find_element('id','search_btn').click() # 20220710 코드 수정

# 검색 결과가 다 나올때까지 걸리는시간 1초
time.sleep(1)

# 데이터를 전체적으로 읽는 부분입니다.
full_html = driver.page_source
soup = BeautifulSoup(full_html,'html.parser')
encyclopedic_list = soup.find_all('div','nkindic_basic api_ani_send _svp_item') # encyclopedic_list 데이터 전체 정의

# 각 항목별 분리하여 추출하고 변수 선언
wiki_name = [] # 네이버 지식백과에서 추출한 제목
wiki_substance = [] # 네이버 지식백과에서 추출한 내용
wiki_origin = [] # 네이버 지식백과에서 추출한 출처

for i in encyclopedic_list:
    # 제목 출력
    name = i.find('a','lnk_tit').get_text() # name 변수에 제목 태그 정의
    wiki_name.append(name) # name에 정의한 제목 태그를 wiki_name 리스트에 append 함수로 추가
    print('제목 :',name.strip()) # 제목 : 출력 or 정의된 name 태그를 strip 함수로 문자열 및 공백 제거
    
    # 내용 출력
    substance = i.find('div','api_txt_lines desc').get_text() # substance 변수에 제목 태그 정의
    wiki_substance.append(substance) # substance에 정의한 제목 태그를 wiki_substance 리스트에 append 함수로 추가
    print('내용 :',substance.strip()) # 제목 : 출력 or 정의된 substance 태그를 strip 함수로 문자열 및 공백 제거
    
    # 출처 출력
    origin =i.find('div','nkindic_source elss').get_text() # origin 변수에 제목 태그 정의
    wiki_origin.append(origin) # origin에 정의한 제목 태그를 wiki_origin 리스트에 append 함수로 추가
    print('출처 :',origin.strip()) # 제목 : 출력 or 정의된 origin 태그를 strip 함수로 문자열 및 공백 제거
    print('\n') # 출력 하나 할때마다 밑으로 줄바꿈 함

#xls 파일로 저장
wiki_naver = pd.DataFrame()
wiki_naver['제목'] = wiki_name # xls 파일 제목 부분
wiki_naver['내용'] = wiki_substance # xls 파일 내용 부분
wiki_naver['출처'] = wiki_origin # xls 파일 출처 부분

wiki_naver.to_excel(fx_name, sheet_name='지식백과')

print('xls 파일 저장 경로 : %s' %fx_name) # 파일 저장 경로