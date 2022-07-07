# hokma_crawling_1
[웹 크롤링 기초]

#출처: https://coding-kindergarten.tistory.com/22

* html의 구조
- 태그로 감싸진 내용들의 모음
- 태그란? h1-h6, p, div, span, img, a, ul, ol등을 말함
- 속성명: 태그에 속성을 부여하여 태그를 구분한다.
- ex: 
1)ID: 하나의 웹페이지에 하나만 쓸 수 있는 고유한 이름
2)CLASS: 비슷한 형태를 가진 요소에 여러번 사용할 수 있는 이름

* CSS의 구조
- html로 만들어진 밋밋한 화면을 예쁘게 꾸며주는 역할을 한다.
- 선택자(selector)와 선언부(declaratives)로 구성

* python web crawling package
1. requests
- html 문서를 가져올 때 사용하는 패키지.
2. selenium
- chromedriver을 이용해 chrome을 제어하기 위해 사용.
- 어떤 값을 입력하거나 특정 버튼을 누를 때 사용
3. beautifulsoup

* 정적 웹 페이지 vs 동적 웹 페이지
1) 정적 웹 페이지: 
- 서버(Web Server)에 미리 저장된 파일이 그대로 전달되는 웹 페이지를 말합니다.
- 따라서 url 주소 외에는 아무것도 필요없다.
ex) requests/urllib 사용, parsing package: bs4

parsing: 복잡한 html 문서를 분류, 정리하는 것

* 정적 수집
멈처있는 페이지의 html을 requests 혹은 urllib로 가져와서 bs4로 파싱하여 원하는 정보 수집

2) 동적 웹 페이지: 
- url 만으로는 들어갈 수 없는 웹페이지
- url의 변화가 없는데도 실시간으로 내용이 계속해서 추가되거나 수정 될 때
ex) selenium 사용, parsing package: bs4, selenium

* 동적 수집
동적 수집은 계속 움직이는 페이지를 다루기 위해서 selenium 패키지로 chromdriver를 제어
특정 url로 접속해서 로그인을 하거나 버튼을 클릭하는 식으로 원하는 정보가 있는 페이지로 접속

이때 driver.find_elements_by_ 함수를 이용해 html을 곧바로 지목해서 추출할 수도 있고, driver.page_source 함수를 이용해 전체 html을 받아 올 수도 있습니다. 

