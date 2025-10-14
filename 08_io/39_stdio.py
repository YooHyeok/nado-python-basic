print("Python", "Java")
print("Python" + "Java")

print("Python", "Java", sep = ",") # sep는 구분자로 기본값은 공백이다.
print("Python", "Java", "javascript", sep = " vs ")

print("Python", "Java", sep = ",", end="?") # end는 문장의 마지막 출력 문자로 기본값은 \n이다.
print("무엇이 더 재밌을까요?")

# sys. stdout, stderr
import sys
print("Python", "Java", file=sys.stdout) # 표준 출력 처리(콘솔)
print("Python", "Java", file=sys.stderr) # 표준 에러 처리 - 로깅 처리를 위해 사용 

# ljust, rjust
# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100} # Dictionary
for subject, score in scores.items(): # dict_items([(key, value), ...]) 형태의 데이터에서 key, value pair를 tuple로 언패킹 하여 내보낸다.
  print(
    subject.ljust(8), # ljust(n): n칸의 공간 확보하고 좌측정렬
    str(score).rjust(4), # rjust(n): n칸의 공간을 확보하고 우측정렬
    sep=" : "
  )

# zfill(n) - n만큼의 크기, 공간을 확보하여 값을 채우되, 값이 없는 빈공간은 0으로 채운다.
# 은행 대기 순번표 - 001, 002, 003, 00n
for num in range(1, 21):
  print("대기번호 : " + str(num).zfill(3))

# input(): 표준 입력 (사용자 입력을 통해 값을 받게되면 항상 문자열 형태로 저장)
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")