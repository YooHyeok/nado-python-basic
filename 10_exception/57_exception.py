""" 
[예외처리]
예외처리란 어떤 에러가 발생했을 때 그에 대해서 처리 해주는것을 말한다.  
계산기에 숫자를 입력받아야 하는데 문자를 입력받았다던지 혹은 홈페이지에 접속 했는데 주소를 잘못 적거나  
사용자가 많아 서버에 문제가 생겨 접속이 잘 되지 않는 현상도 에러라고 볼 수 있다.  
이렇게 예외처리 구문을 이용해서 없는 파일을 열려고 한다던지,  
리스트에 없는 값을 잘못 접근 한다던지 등과 같은 문제가 발생 했을 때,  
프로그램이 강제 종료되는 것을 막음으로써 프로그램의 완성도를 높일 수 있다.
 """

def example1():
	print("나누기 전용 계산기 입니다.")
	num1 = int(input("첫 번째 숫자를 입력하세요 : ")) # 6 | 6
	num2 = int(input("두 번째 숫자를 입력하세요 : ")) # 3 | 삼 
	print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) # 6 / 3 = 26 | 6 / 삼 = error

def example2():
	try:
		print("나누기 전용 계산기 입니다.")
		num1 = int(input("첫 번째 숫자를 입력하세요 : ")) # 6 | 6
		num2 = int(input("두 번째 숫자를 입력하세요 : ")) # 3 | 삼 
		print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) # 6 / 3 = 26 | 6 / 삼 = error
	except ValueError:
		print("에러! 잘못된 값을 입력하였습니다.")
	except ZeroDivisionError as err:
		print(err)

def example3():
	try:
		print("나누기 전용 계산기 입니다.")
		nums = []
		nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) # 6 | 6
		nums.append(int(input("두 번째 숫자를 입력하세요 : "))) # 3 | 삼
		# nums.append(int(nums[0] / nums[1]))
		print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2])) # 6 / 3 = 26 | 6 / 삼 = error
	except ValueError:
		print("에러! 잘못된 값을 입력하였습니다.")
	except ZeroDivisionError as err:
		print(err)
	except Exception as err:
		print("알 수 없는 에러가 발생하였습니다.")
		print(err)

example3()