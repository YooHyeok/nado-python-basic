# 리스트 []

# 지하철 칸 별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30] # subway라는 하나의 변수안에 10, 20, 30을 넣어 묶어줌.
print(subway)

subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호")) # index(): 리스트의 요소에서 넘겨받은 문자열 탐색 후 index 위치를 반환

# 요소 포함 여부
print("조세호" in subway)

# 하하씨가 당음 정류장에서 다음 칸에 탐
subway.append("하하") # append(): 리스트의 가장 마지막에 삽입.
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재혁씨와 조세호씨 사이에 태워봄
subway.insert(1, "정형돈") # 유재혁씨와 조세호씨 사이 위치는 1번 인덱스
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop()) # pop(): 리스트의 가장 마지막 요소 삭제 후 삭제된 요소를 반환
print(subway) # ['유재석', '정형돈', '조세호', '박명수']

# 3회 반복
print(subway.pop()) # 박명수 (삭제)
print(subway) # ['유재석', '정형돈', '조세호']
print(subway.pop()) # 조세호 (삭제)
print(subway) # ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") # ['유재석', '정형돈', '유재석']
print(subway)
print(subway.count("유재석")) # 2명

# 정렬 - sort()
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 역순 - reverse()
num_list.reverse()
print(num_list)

# 모두 삭제 - clear()
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_lit = ["조세호", 20, True]
print(mix_lit)

# 리스트 결합 - list1.extend(list2)
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_lit)
print(num_list)