""" 
set(집합)
중복 불가 및 순서가 존재하지 않는다.
{}중괄호를 사용한다.
"""
my_set = {1, 2, 3, 3, 3}
print(my_set) # 중복을 허용하지 않으므로 1, 2, 3만 출력

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # list를 먼저 선언한 후 set() 생성자에 전달하여 변환 가능

# 교집합: & 혹은 intersection()
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합: | 혹은 union() 함수 - 순서를 보장하지 않는다.
print(java | python) # {'박명수', '유재석', '양세형', '김태호'}
print(java.union(python)) # {'박명수', '유재석', '양세형', '김태호'}

# 차집합: - 혹은 difference() 함수
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# set에 값 추가: add() 함수
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}

# set에서 값 삭제: remove() 함수
python.remove("김태호")
print(python) # {'유재석', '박명수'}
