# 네이버 'VIEW' 섹션의 내용 수집하기
# 검색 키워드 입력 : 봄 여행
# 파일 저장(txt) : C:\python_temp\data\test.txt

import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

# 검색할 키워드를 입력 하는 부분
search_txt = input("검색할 키워드를 입력해주세요 : ")

# 파일 경로를 입력하는 부분
fi_a = input('검색결과를 저장할 파일 경로와 이름을 지정하세요.\n(예: C:\\Python_temp\\data\\text.txt) : ')

server = 'C:\\web_driver\\chromedriver.exe'
driver = webdriver.Chrome(server) # 크롬으로 실행함
driver.get('https://www.naver.com/') # 크롬 브라우저 안에 naver 사이트 실행

#검색창에 키워드를 넣는 부분
element = driver.find_element('id','query') # 검색창에 입력 / 20220710 코드 수정
element.send_keys(search_txt) # search_txt에서 입력 받은 키워드를 넣음
time.sleep(2) # 검색창에 키워드를 입력하는 시간 2초

# 네이버 검색창 우측 돋보기 모양 검색 버튼을 클릭합니다.
element = driver.find_element('id','search_btn').click() # 20220710 코드 수정

# 검색 결과가 나올때까지 기다리는 시간 1초 소요
time.sleep(1)

#txt 파일로 저장하는 부분
t_stdout = sys.stdout
f = open(fi_a,'a',encoding='UTF-8')
sys.stdout = f
time.sleep(1)

# 데이터를 전체적으로 읽는 부분
full_html = driver.page_source
soup = BeautifulSoup(full_html,'html.parser')
springtime_list = soup.find_all('li', 'bx _svp_item') # springtime_list 데이터 전체 정의

# 각 항목별 리스트로 변수 정의
figure = 1 # 번호 출력할때 사용할 값
figure2 = [] # 반복문 이용해서 9번까지 출력할 리스트 변수
view_origin = [] # naver view에서 추출할 출처
view_name = [] # naver view에서 추출할 제목
view_substance = [] # naver view에서 추출할 내용
view_hashtag=[] # naver view에서 추출할 해시태그


try : # 예외처리 try 문 사용
    for i in range(len(springtime_list)): # springtime_list 길이 만큼 반복합니다.
        #번호를 출력 하는 부분
        figure2.append(figure) # frgure2 변수 안에 append 함수로 figure 추가
        print('번호 : {}'.format(figure)) # 번호를 출력하는 부분
        figure += 1  # 번호 출력 총 9번 반복인데 하나 늘어날때마다 1씩 + 함
    
        # 출처를 출력 하는 부분
        origin = springtime_list[i].find('a','sub_txt sub_name').get_text()
        view_origin.append(origin) # view_origin에 append 함수로 orgin 추가
        print('출처 :',origin.strip()) # 출처를 출력합니다.
    
        # 제목을 출력하는 부분
        name = springtime_list[i].find('a','api_txt_lines total_tit _cross_trigger').get_text()
        view_name.append(name) # view_name에 append 함수로 name 추가
        print('제목 :',name.strip()) # 제목을 출력합니다.
    
        # 내용을 출력하는 부분
        substance = springtime_list[i].find('div','api_txt_lines dsc_txt').get_text()
        view_substance.append(substance)  # view_substance에 append 함수로 substance 추가
        print('내용 :',substance) # 내용을 출력합니다 
    
        # 해시태그를 출력하는 부분
        hashtag = springtime_list[i].find('div','total_tag_area').get_text()
        view_hashtag.append(hashtag)  # view_hashtag에 append 함수로 hashtag 추가
        print('태그 :',hashtag) # 해시태그를 출력합니다.
        print('\n') # \n 으로 출력 하나 할때마다 밑으로 줄바꿈 함
# except 문으로 에러 발생시 에러 코드 입력후 pass
except AttributeError:
    pass
    
sys.stdout = t_stdout
f.close()
print('txt 파일 저장 경로 : %s' %fi_a) # 파일 저장 경로 출력