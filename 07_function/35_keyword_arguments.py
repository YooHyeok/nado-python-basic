# [키워드 인자(인수)]
def profile(name, age, main_lang):
  print(name, age, main_lang)

profile("유재석", 20, "파이썬") # 기본 매개변수 전달(순서기반 인자)

# 키워드 인자(인수) 시작 - 매개변수 순서를 자유롭게 지정할 수 있으며, 매개변수 가독성이 좋아지는 장점이 있어 실수를 방지할 수 으나, 코드가 길어지고 컴파일 시점에 변수명을 체킹할 수 없어 변수명 오타 등의 이유로 오류를 유발할 수 있다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")