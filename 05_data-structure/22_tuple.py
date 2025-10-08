""" 
튜플
리스트와 다르게 내용을 변경하거나 추가할 수 없음
리스트보다 속도가 빠르다.
() 괄호를 사용한다.
"""

menu = ("돈까스", "치즈까스")
print(menu)
print(menu[1]) # 접근: 구독연산

# 튜플 활용
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

""" 
언패킹: 묶여있는(패킹된) 데이터를 풀어서(언패킹) 개별 변수에 할당하는 것
"""
name, age, hobby = "김종국", 20, "코딩" # 
print(name, age, hobby)
