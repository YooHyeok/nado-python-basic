""" 
[피일 입출력 예제]
"""

score_file = open("score.txt", "w", encoding="utf8") # w: 쓰기 / utf8: 한글깨짐 방지를 위함
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # a: 추가(이미 내용이 존재하는 파일에 이어서 추가)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# read(): 모든 내용 읽기
score_file = open("score.txt", "r", encoding="utf8") # r: 읽기
print(score_file.read()) # 파일에 있는 모든 내용일 읽어온다.
score_file.close()

# readline(): 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # readline(): 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print()
score_file.close()

# 한줄씩 읽고 반복문으로 출력
score_file = open("score.txt", "r", encoding="utf8")
while True:
	line = score_file.readline()
	if not line: break
	print(line, end="")
print()
score_file.close()

# readlines(): 모든 라인을 읽어 list 형태로 저장
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
	print(line, end="")
print()
score_file.close()