from bs4 import BeautifulSoup as bs
import requests


url = 'https://www.ewha.ac.kr/ewha/guide/sitemap.do'

response = requests.get(url)
html_text=response.text
soup = bs(html_text, 'html.parser')
titles = []
for n in range(93,107):
    a = soup.select_one('li[id = ]#menu'+str(n))
    print(a.get_text)
