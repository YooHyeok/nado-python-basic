# [가변인자]
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
  print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # print에서 end의 기본값은 "\n" 으로 줄개행이 적용된다. end 매개변수를 임의로 지정할 경우 줄바꿈대신 다른 문자를 지정할 수 있다.
  print(lang1, lang2, lang3, lang4, lang5)
profile("유재석", 20, "Python", "Java", "C", "Rust", "GoLang")
profile("김태호", 25, "Kotlin", "Swift", "", "", "") # 사용 가능한 언어가 5개보다 적을경우 매번 빈값을 넣어줘야한다.


def profile(name, age, *language):
  print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # print에서 end의 기본값은 "\n" 으로 줄개행이 적용된다. end 매개변수를 임의로 지정할 경우 줄바꿈대신 다른 문자를 지정할 수 있다.
  for lang in language:
    print(lang, end=" ")
  print()

profile("유재석", 20, "Python", "Java", "C", "Rust", "GoLang", "TypeScript") # 사용 가능 언어 6개
profile("김태호", 25, "Kotlin", "Swift") # 사용 가능 언어 2개