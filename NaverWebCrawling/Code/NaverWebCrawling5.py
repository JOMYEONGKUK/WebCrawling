# 네이버 '뉴스' 섹션의 내용 수집하기
# 검색 키워드 입력 : 봄 여행
# 파일 저장(txt) : C:\python_temp\data\test_20220222_Ex04.txt

import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

# 검색창에 키워드를 입력합니다.
news_txt = input("검색할 키워드를 입력해주세요 : ")

# 파일 저장 경로를 입력해주세요.
file_pro = input("검색결과를 저장하는 파일 경로 이름을 지정해주세요.\n(예: C:\\Python_temp\\data\\text.txt) : ")

server = 'C:\\web_driver\\chromedriver.exe'
driver = webdriver.Chrome(server) # 크롬으로 실행함
driver.get('https://www.naver.com/') # 크롬 브라우저 안에 naver 사이트 실행

# 검색창에 키워드를 넣는 부분입니다.
element = driver.find_element('id','query') # 20220710 코드 수정
element.send_keys(news_txt) # news_txt에서 입력 받은 키워드를 넣음
time.sleep(2) # 검색창에 키워드를 입력하는 시간 2초 걸림

# 네이버 검색창 우측 돋보기 모양 검색 버튼을 클릭합니다.
element = driver.find_element('id','search_btn').click() # 20220710 코드 수정

# 검색 결과가 나올때까지 걸리는 시간 1초 소요
time.sleep(1)

# txt 파일로 저장하는 부분
t_stdout = sys.stdout
f = open(file_pro, 'a', encoding='UTF-8')
sys.stdout = f
time.sleep(2) # txt 파일로 저장하는데 걸리는 타임 2초 소요

# 데이터를 전체적으로 읽는 부분
full_html = driver.page_source
soup = BeautifulSoup(full_html,'html.parser')
news_list = soup.find_all('div','news_wrap api_ani_send') # news_list 데이터 전체 정의

# 각 항목별 분리하여 추출하고 변수 할당
num = 1 # 번호를 출력할때 사용할 값
number = [] # 번호 표시할 변수 리스트 num을 담을 곳
news_pressa = [] # news 에서 추출할 언론사명
news_name = [] # news 에서 추출할 기사 제목
news_contents = [] # news 에서 추출할 기사 내용

for i in news_list:
    #번호를 출력
    number.append(num) # number 리스트안에 append 함수로 num 추가
    print('번호 : {}'.format(num)) # 번호를 출력하는 프린트
    num += 1 # 번호 출력 총 4번 중 한번씩 반복될때마다 1씩 + 함
    
    # 언론사를 출력
    pressa = i.find('a','info press').get_text() # pressa 변수에 언론사 태그 정의
    news_pressa.append(pressa) # pressa에 정의한 언론사 태그를 news_pressa 리스트에 append 함수로 추가
    print('언론사 :',pressa.strip()) # 언론사 : 출력 or 정의된 pressa 태그를 strip 함수로 문자열 및 공백 제거
    
    # 제목 출력
    name = i.find('a','news_tit').get_text() # name 변수에 언론사 태그 정의
    news_name.append(name) # name에 정의한 언론사 태그를 news_name 리스트에 append 함수로 추가
    print('제목 :',name.strip()) # 제목 : 출력 or 정의된 name 태그를 strip 함수로 문자열 및 공백 제거
    
    # 내용 출력
    content =i.find('a','api_txt_lines dsc_txt_wrap').get_text() # content 변수에 언론사 태그 정의
    news_contents.append(content) # content에 정의한 언론사 태그를 news_contents 리스트에 append 함수로 추가
    print('내용 :',content.strip()) # 내용 : 출력 or 정의된 content 태그를 strip 함수로 문자열 및 공백 제거
    print('\n') # 출력 하나 할때마다 밑으로 줄바꿈 함

sys.stdout = t_stdout
f.close()
print('txt 파일 저장 경로 : %s' %file_pro) # 파일 저장 경로 출력