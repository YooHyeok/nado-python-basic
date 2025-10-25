""" 
모듈 파일
사용하려는 클래스에서 import하여 사용한다.
모듈을 사용하려는 파일과 같은 경로에 있거나, 파이썬 라이브러리들이 모여있는 폴더에 있어야 사용이 가능하다.
"""

# 일반 가격
def price(people):
	print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):
	print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 조조 할인 가격
def price_soldier(people):
	print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))

class Hi:
	def __init__(self):
		print("Hi")