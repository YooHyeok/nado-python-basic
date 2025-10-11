# for

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

# for {변수} in [리스트]
for waiting_num in [0, 1, 2, 3, 4]:
  print("대기번호: {0}".format(waiting_num))

# for {변수} in range(x) 0부터 ~ x-1까지 범위
for waiting_num in range(5): # 0, 1, 2, 3, 4
  print("대기번호: {0}".format(waiting_num))

# for {변수} in range(x, y) x부터 y까지 범위
for waiting_num in range(1, 6): # 1, 2, 3, 4, 5
  print("대기번호: {0}".format(waiting_num))
  
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
  print("{0}, 커피가 준비되었습니다.".format(customer))