""" 
[예외처리 - 에러 발생시키기]
raise 키워드를 통해 에러를 발생시킨다.
자바에서 throw와 같다.
"""

try:
	print("한 자리 숫자 나누기 전용 계산기입니다.")
	num1 = int(input("첫 번째 숫자를 입력하세요 : "))
	num2 = int(input("두 번째 숫자를 입력하세요 : "))
	if num1 >= 10 or num2 >= 10:
		raise ValueError
	print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError: # raise에 의해 실행됨 - 숫자 두개중 하나가 10보다 클 경우 해당 구분으로 진입
	print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")