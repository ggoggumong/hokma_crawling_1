#step1.프로젝트에 필요한 패키지 불러온다.
from bs4 import BeautifulSoup as bs
import requests

#step2.만약 다른 키워드를 매번 다르게 입력하고 싶다면 아래와 같이 하셔도 됩니다.
query = input('검색할 키워드를 입력하세요: ')
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'%s'%query

#step3.requests 패키지의 함수를 이용해 url의 html 문서를 가져온다.
response = requests.get(url)
html_text=response.text

#step4.bs4 패키지의 함수를 이용해서 html 문서를 파싱한다.
soup = bs(html_text, 'html.parser')

#step5.bs4 패키지의 select_one 함수와 선택자 개념을 이용해서 뉴스기사 제목을 하나 가져온다.
print(soup.select_one('a.news_tit').get_text())

#step6.bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 모두 가져온다.
titles = soup.select('a.news_tit')

for i in titles:
    title = i.get_text()
    print(title)

# get_text( ) 함수는 반드시 1개의 html 태그에만 사용할 수 있다.
# 꼭 for문으로 하나하나씩 가져오기