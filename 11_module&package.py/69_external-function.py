""" 
[외장함수]: 내장함수와는 다르게 직접 import 해서 사용해야한다.
Python Module Index
외장함수 목록을 확인할 수 있다.
구글 검색창에 `list of python modules` 검색
 """

# glob: 경로 내 폴더/파일 조회(윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 조회

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시

## 폴더 추가 삭제 예제
folder = "sample_dir"
if os.path.exists(folder): # 해당 폴더가 존재한다면?
  print("이미 존재하는 폴더입니다.")
  os.rmdir(folder)
  print(folder, "폴더를 삭제하였습니다.")
else:
  os.makedirs(folder) # 폴더 생성
  print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) # 현재 실행된 모듈이 위치한 디렉토리 하위 디렉토리 및 파일을 모두 출력

# time: 시간 관련 함수
import time
print(time.localtime()) # time.struct_time(tm_year=2025, tm_mon=10, tm_mday=20, tm_hour=10, tm_min=30, tm_sec=33, tm_wday=0, tm_yday=293, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S")) # yyyy-MM-dd HH:mm:SS

import datetime
print("오늘 날짜는", datetime.date.today())

# timedata: 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은",today + td) # 오늘부터 100일 후