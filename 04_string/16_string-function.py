python = "Python is Amazing"

print(python.lower()) # 문자열 소문자로 반환
print(python.upper()) # 문자열 대문자로 반환

print(python[0].isupper()) # 문자가 대문자인지 여부 확인
print(python[0].islower()) # 문자가 소문자인지 여부 확인

print("PYTHON IS AMAZING".isupper()) # 문자열일 경우 모든 문자가 대문자여야 True를 반환(띄어쓰기는 무시)

print(len(python)) # len(): 문자열의 길이 반환 함수

print(python.replace("Python", "Java")) # replace(): 문자열 부분 치환 함수 - Python 문자열을 찾아 Java로 변경.

index = python.index("n") # index(): 문자열에서 전달받은 문자(열)의 위치 - 탐색하려는 값이 없을 경우 오류 발생(프로그램 종료)
print(index) # 5

index = python.index("n", index + 1) # 두번째 매개변수에 정수 전달 가능 - 탐색을 시작할 위치
print(index) # 15 (5 위치부터 n 탐색)

print(python.find('Java')) # find(): 문자열 위치 탐색 - 탐색하려는 값이 없을경우 오류가 아닌 -1 반환

print(python.count("n")) # # count(): 전달받은 문자열이 몇번 등장하는지 계산