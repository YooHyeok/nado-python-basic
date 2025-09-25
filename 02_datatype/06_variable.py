print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

print("우리집 강아지의 이름은 해피에요")
print("해피는 4살이며, 산책을 아주 좋아해요")
print("해피는 어른일까요? True")

animal = "강아지"
name = "해피"
age = 4
hobby = "산책"
is_adult= age >= 3 # 나이가 3살 이상이면 어른

print("우리집 " + animal + " 이름은 " + name + " 해피에요")

print(name + "는 " + str(age) + "살이며, " + hobby +"을 아주 좋아해요") #  +연산자를 포함한 정수를 print문에서 사용하기 위해서는 str() 이라는 함수를 사용하여 문자로 변경한다.
print(name + "는 어른일까요?" +  str(is_adult)) # python에서 논리 자료형은 숫자의 서브클래스(True: 1/ False: 0) 이므로 마찬가지로 str()을 사용한다.

# ,로 출력할 경우 정수 혹은 논리 자료형을 str()을 사용하지 않고 그대로 사용 가능하다. (,의 경우 띄어쓰기가 포함된다.)
print(name, "는 ", age, "살이며, ", hobby,"을 아주 좋아해요")
print(name, "는 어른일까요?", is_adult)