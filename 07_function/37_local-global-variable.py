""" 
[지역변수와 전역변수]
- 지역변수: 함수가 호출되었다가 함수 호출이 끝나면 사라지는것을 지역변수라고 한다.
- 전역변수: 프로그램 내 어디서든 접근할 수 있는 변수이다.
"""
gun = 10
def checkpoint(soldiers): # 경계 근무
	# gun = 20 # 지역변수를 선언하지 않으면 오류 발생
	global gun # global 키워드를 사용하여 전역 공간에 있는 gun을 사용
	gun = gun - soldiers
	print("[함수 내] 남은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 전역변수를 함수 내에서 사용하지 않고, 매개변수로 전달하여 관리
def checkpoint_return(gun, soldiers):
	gun = gun - soldiers
	print("[함수 내] 남은 총 : {0}".format(gun))
	return gun
print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))