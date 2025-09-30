from random import *

print(random()) # 0.0 ~ 1.0 미만의 임이의 값 생성
print("[1 ~ 10 미만 실수]")
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print("[1 ~ 10 미만 정수]")
print(int(random() * 10)) # int(): 파이썬 내장함수로 정수로 반환(소수라면 정수 부분만 반환)
print(int(random() * 10))
print(int(random() * 10))

print("[1 ~ 10 이하]")
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print("[로또 번호 생성]")
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성 - 로또 범위
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print("[로또 번호 생성: randrange]")
print(randrange(1, 46)) # randrange: 1 ~ 46 미만의 값 생성
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print("[로또 번호 생성: randint]")
print(randint(1, 45)) # randint: a, b 사이의 숫자 중 양 끝을 모두 포함하여 랜덤으로 추출