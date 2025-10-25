""" 
[예외처리 - 사용자 정의 예외처리]

"""

class BigNumberError(Exception):
	pass

def example1():
	try:
		print("한 자리 숫자 나누기 전용 계산기입니다.")
		num1 = int(input("첫 번째 숫자를 입력하세요 : "))
		num2 = int(input("두 번째 숫자를 입력하세요 : "))
		if num1 >= 10 or num2 >= 10:
			raise BigNumberError
		print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
	except ValueError: # raise에 의해 실행됨 - 숫자 두개중 하나가 10보다 클 경우 해당 구분으로 진입
		print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
	except ZeroDivisionError as err:
		print(err)
	except BigNumberError:
		print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")


class BigNumberError(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return self.msg

def example2():
	try:
		print("한 자리 숫자 나누기 전용 계산기입니다.")
		num1 = int(input("첫 번째 숫자를 입력하세요 : "))
		num2 = int(input("두 번째 숫자를 입력하세요 : "))
		if num1 >= 10 or num2 >= 10:
			raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
		print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
	except ValueError: # raise에 의해 실행됨 - 숫자 두개중 하나가 10보다 클 경우 해당 구분으로 진입
		print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
	except ZeroDivisionError as err:
		print(err)
	except BigNumberError as err:
		print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
		print(err)

example2()