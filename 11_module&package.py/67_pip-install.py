""" 
[pip install]
패키지를 설치하는 명령이다.
pypi: `https://pypi.org/`
Beautifulsoup - 웹 스크래핑 패키지

- 패키지 설치 명령: `install`
  ```bash
  pip install beautifulsoup4
  ```
- 현재 설치되어있는 패키지 목록 확인: list
  ```bash
  pip list
  ```
- 패키지 상세 정보 확인: `show`
  ```bash
  pip show beautifulsoup4
  ```
- 패키지 최신버전 업그레이드: `install --upgrade`
  ```bash
  pip install --upgrage beautifulsoup4
  ```
- 삭제 명령: `uninstall`
  ```bash
  pip uninstall beautifulsoup4
  ```
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())