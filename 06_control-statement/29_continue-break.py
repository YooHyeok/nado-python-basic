# continue: 반복문의 처음으로 돌아가 다음 요소부터 반복
# break: 반복문 종료

# 출석번호를 추첨하여 책을 읽히게 한다.

absent = [2, 5] # 결석
no_book = [7] # 책을 가져오지 않음
for student in range(1, 11): 
  if student in absent: # 현재 요소가 리스트에 포함되었다면
    continue # 반복문의 처음으로 돌아가 다음 반복
  if student in no_book: # 현재 요소가 리스트에 포함되었다면
    print("오늘 수업 여기까지. {0}는 교뮤실로 따라와".format(student))
    break # 반복문 종료
  print("{0}, 책을 읽어봐".format(student))