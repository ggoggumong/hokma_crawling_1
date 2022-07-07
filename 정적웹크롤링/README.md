#1. 정적 수집의 순서

1단계. 목표로 하는 웹 페이지의 html을 requests 패키지를 이용하며 받아 옴

2단계. 가져온 html 문서 전체를 beautifulsoup4 패키지를 이용하여 파싱(parsing)함

3단계. 필요한 정보만 골라서 리스트에 담음.

4단계. 리스트를 print() 함수로 출력하던가, excel이나 csv 파일에 저장.

 