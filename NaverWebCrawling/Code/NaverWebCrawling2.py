# 네이버 빅데이터 로 검색한 후, 뉴스 섹션의 정보를 수집하기

import requests
from bs4 import BeautifulSoup

req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# bigdata_list 변수 정의 li class bx 전체 정의
bigdata_list = soup.find_all('li', class_='bx')
for i in range(len(bigdata_list)): # 반복문으로 big_data_list 길이에 맞춰서 반복함
    try:
        # 출처, 시간, 내용 출력
        print('source time :',bigdata_list[i].find('div', class_='info_group').get_text())
        print('news title :',bigdata_list[i].find('a', class_='news_tit').get_text())
        print() # 한칸 공백 남겨놓고 출력
        print('contents :',bigdata_list[i].find('div', class_='dsc_wrap').get_text())
        print() # 한칸 공백 남겨놓고 출력
    # except 문으로 에러 발생시 패스
    except AttributeError:
        pass