# while

customer = "토르"
index = 5
while index >= 1 :
  print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
  index -= 1
  if index == 0:
    print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
while True:
  if index == 101: break
  print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
  index += 1

customer = "아이언맨"
person = "Unknown"
while person != customer: # 아이언맨 일 경우 반복문 종료
  print("{0}, 커피가 준비 되었습니다.".format(customer))
  person = input("이름이 어떻게 되세요?")

index = 0
while index != 101: # if문을 넣어 break하지않고 처리
  print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
  index += 1