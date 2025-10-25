""" 
[예외처리 - finally]
예외처리 구문에서 정상적으로 수행이 되건, 오류가 발생하건 상관없이 무조건 실행되는 구문이다.
try 구문 제일 마지막에 작성할 수 있다.
"""

class BigNumberError(Exception):
	pass

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
finally:
  print("계산기를 이용해 주셔서 감사합니다.")
    
