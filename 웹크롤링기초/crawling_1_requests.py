import requests
url = 'https://www.naver.com'
response = requests.get(url)

print(response.status_code)
html_text = response.text

print(html_text)