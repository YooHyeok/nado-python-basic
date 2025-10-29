""" 
[내장 함수]
Built-in Functions
파이썬 내에서 사용 가능한 내장 함수를 확인할 수 있다.
구글 검색창에 `list of python builtins` 입력

"""

# input: 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir()) # 현재 사용 가능한 모듈
import random # 외장 모듈 추가
print(dir()) # 현재 사용 가능한 모듈에 random 추가 확인됨
import pickle # 외장 모듈 추가
print(dir()) # 현재 사용 가능한 모듈에 pickle 추가 확인됨
print(dir(random)) # random 모듈 내에서 사용 가능한 함수 목록

list = [1, 2, 3]
print(dir(list)) # list에서 사용 가능한 함수 목록 출력

name = "jim"
print(dir(name)) # string에서 사용 가능한 함수 목룍 출력