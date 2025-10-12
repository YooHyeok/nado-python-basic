def profile(name, age, main_lang):
  print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang)) # 다음라인으로 \를 사용한다. (과거스타일)
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# [기본 매개변수] 같은학교, 같은학년, 같은반, 같은수업 일 때 기본 값을 사용할 수 있다.
def profile(name, age=17, main_lang="러스트"):
  print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"
        .format(name, age, main_lang))
profile("학생1")
profile("학생2")