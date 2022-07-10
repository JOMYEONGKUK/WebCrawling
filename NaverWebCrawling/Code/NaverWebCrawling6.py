# 네이버 '어학사전' 섹션의 내용 수집하기
# 검색 키워드 입력 : 빅데이터
# 파일 저장(txt) : C:\python_temp\data\test_20220222_Ex06.txt.txt

import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

# 검색할 키워드를 입력하는 부분
Language_txt = input("검색할 키워드 입력 : ")

# 파일 저장 경로를 입력하는 부분
f_name = input('검색결과를 저장할 파일 경로와 이름을 지정하세요.(예: C:\\Python_temp\\data\\text.txt) : ')

folders = 'C:\\web_driver\\chromedriver.exe'
driver = webdriver.Chrome(folders) # 크롬으로 실행함
driver.get('https://www.naver.com/') # 크롬 브라우저 안에 naver 사이트 실행 

#검색창에 키워드 입력하는 부분
element = driver.find_element('id','query') # 검색창 입력 / 20220710 코드 수정
element.send_keys(Language_txt) # search_txt에서 입력 받은 키워드를 넣음
time.sleep(2) # 검색창에 키워드 입력하는데 걸리는 시간 2초

#검색 클릭
element = driver.find_element('id','search_btn').click() #돋보기(검색아이콘) 클릭 / 20220710 코드 수정

# 검색 결과가 다 나올때까지 기다립니다.
time.sleep(1)

#txt 파일로 저장
orig_stdout = sys.stdout
f = open(f_name,'a',encoding='UTF-8')
sys.stdout= f
time.sleep(1)

# 데이터를 전체적으로 읽음
full_html = driver.page_source
soup = BeautifulSoup(full_html,'html.parser')
content_list = soup.find_all('div','dic_area') # content_list 데이터 전체 정의

# 각 항목별 분리하여 추출하고 변수 할당
dic_name = [] # 어학사전에서 추출한 카테고리
dic_title = [] # 어학사전에서 추출한 단어
dic_meaning = [] # 어학사전에서 추출한 단어 뜻


for i in content_list:
    # 제목 출력
    name = i.find('h3','dic_title_sub').get_text()
    dic_name.append(name) # dic_name에 append 함수로 name 추가
    print('제목 :',name.strip()) # 제목을 출력합니다.
    
    # 내용 출력
    title = i.find('a','title').get_text()
    dic_title.append(title) # dic_title에 append 함수로 title 추가
    print('내용 :',title.strip()) # 내용을 출력합니다.
    
    # 뜻
    meaning = i.find('p','mean').get_text()
    dic_meaning.append(meaning) # dic_meaning에 append 함수로 meaning 추가
    print('뜻 :',meaning.strip()) # 출처를 출력합니다.
    print('\n') # 출력 하나 할때마다 밑으로 줄바꿈 함
        
sys.stdout = orig_stdout
f.close()
print('txt 파일 저장 경로 : %s' %f_name) # 파일 저장 경로 출력