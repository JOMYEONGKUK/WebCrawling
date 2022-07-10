#  네이버에 빅데이터로 검색한 후, 지식백과 섹션의 정보를 수집하기
import requests
from bs4 import BeautifulSoup

req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# big_data_lista 변수 정의 div class nkindic_basic 전체 정의
big_data_lista = soup.find_all("div", class_="nkindic_basic")
for i in range(len(big_data_lista)): # 반복문으로 big_data_lista 길이에 맞춰서 반복함
    # 제목 부분 출력합니다.
    print(f'제목 : {big_data_lista[i].find("a", class_="lnk_tit").get_text()}')
    try :
        # big data, Big Data or 빅데이터란 밑부분 글씨 출력
        print(big_data_lista[i].find("span", class_="sub_tit").get_text())
        print(big_data_lista[i].find("span", class_="lnk_sub_tit").get_text())
        # 한칸 공백 남겨놓고 출력
        print()
    # exccept 문으로 에러 발생시 패스
    except AttributeError:
        pass
    # 출처 및 본문 내용 출력
    print(f'본문내용 : {big_data_lista[i].find("div", class_="api_txt_lines").get_text()}')
    print(f'출처 : {big_data_lista[i].find("span", class_="source_txt").get_text()}')
    # 한칸 공백 남겨놓고 출력
    print()