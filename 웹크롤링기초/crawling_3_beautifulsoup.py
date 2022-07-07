import requests

# 주로 bs로 이름을 간단히 만들어서 사용함
from bs4 import BeautifulSoup as bs

response = requests.get('https://www.google.co.kr')

# html을 잘 정리된 형태로 변환
html = bs(response.text, 'html.parser')

# find 함수로 특정 이미지를 선택하는 코드
google_logo = html.find('img', {'id':'hplogo'})