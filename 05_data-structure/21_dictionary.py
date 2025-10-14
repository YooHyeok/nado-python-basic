""" 
사전
일반적으로 사전에서 단어 탐색시 단어 우측으로 설명이 나온다. 
python의 dictionary도 key와 value 형태로 나오게 된다. 
key는 단 하나의 value만 가질 수 있으며 중복될 수 없다.
중괄호를 사용한다.
"""
cabinet = {3:"유재석", 100: "김태호"} # key: 3, value: "유재석" / key: 100 , value: "김태호"

# 접근: 구독연산 - [index] - 값이 없을경우 런타임 오류 발생
print(cabinet[3]) # key가 3에 해당하는 value 출력 - 유재석
print(cabinet[100]) # key가 100에 해당하는 value 출력 - 김태호

# 접근: get(index) - 값이 없을경우 None이 출력되므로 구독 연산보다 안전하게 사용 가능
print(cabinet.get(3))
print(cabinet.get(33)) # 없으면 None이 출력되므로 안전하다. (None은 자바에서 null)
print(cabinet.get(5, "기본")) # 없으면 2번째 매개변수에 전달한 값을 반환 - 자바 Map의 getOrDefault와 같음

# key 포함 여부: in
print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 신규 추가 및 변경
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["c-20"] = "조세호" # 값 추가
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호', 'c-20': '조세호'}
cabinet["A-3"] = "김종국" # 값 변경
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'c-20': '조세호'}

# 제거 - del 키워드
del cabinet["A-3"]
print(cabinet)

# key만 혹은 value만, 혹은 모든 item을 출력
print(cabinet.keys()) # dict_keys(['B-100', 'c-20'])
print(cabinet.values()) # dict_values(['김태호', '조세호'])
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('c-20', '조세호')])

# 모두 삭제 - clear()
cabinet.clear()
print(cabinet) # {}
