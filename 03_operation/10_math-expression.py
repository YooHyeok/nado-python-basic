# 연산 우선순위
print(2 + 3 * 4) # 곱셈 우선순위 - 14
print((2 + 3) * 4) # 괄호 결합법칙 - 20
number = 2 + 3 * 4 
print(number) # 14 출력

# 복합 대입 연산 - 변수에 연산 후 결과를 변수에 다시 대입
number = number + 2 # number에 2를 더한 뒤 다시 number에 대입
print(number) # 16
number += 2 # number에 2를 더한 뒤 다시 number에 대입
print(number) # 18
number *= 2 # number에 2를 곱한 뒤 다시 number에 대입
print(number) # 36
number /= 2 # number에 2를 나눈 뒤 다시 number에 대입
print(number) # 18
number -= 2 # number에 2를 뺀 뒤 다시 number에 대입
print(number) # 16
number %= 2 # number를 2로 나눈 나머지를 number에 대입
print(number) # 0 (나누어 떨어졌기 때문에 나머지가 0)

number = 16
number %= 5 # number를 5로 나눈 나머지를 number에 대입
print(number) # 1 (나머지가 1)