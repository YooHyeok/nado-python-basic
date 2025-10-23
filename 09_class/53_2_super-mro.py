""" 
# 번외. super() mro

Python의 super()는 MRO(Method Resolution Order)를 따라 동작한다.
MRO(Method Resolution Order)는 메소드 결정 순서로, Python이 다중 상속시 어떤 순서로 부모 클래스의 메소드를 찾을 지 결정하는 규칙이다.  

1. 자식 클래스가 부모보다 먼저 호출
2. 부모 클래스는 상속 선언 순서대로 호출
3. 공통 조상(object)은 마지막에 호출

- 다이아몬드 상속시 중복 호출 문제 발생
- MRO를 무시하여 예상치 못한 동작 가능
- 부모 클래스 변경 시 모든 자식 클래스 수정 필요
"""

"""
## 일반 super() MRO 예제

FlableUnit의 super() → Flyable 호출
Flable의 super() → Unit 호출 (Flyable 다음이 Unit)
Unit의 super() → object 호출
 """
class Unit:
  def __init__(self):
    print("Unit 생성자")
    super().__init__()

class Flyable:
  def __init__(self):
    print("Flyable 생성자")
    super().__init__()

class FlableUnit(Flyable, Unit):
  def __init__(self):
    super().__init__()

dropship = FlableUnit() # Flyable 생성자 출력



""" 
## 다이아몬드 상속에서의 super() mro 예제

이때 최상위 공통 부모 Unit은 한번 생성된다.
이전의 53_super.py에서 명시적 클래스 접근을 통한 부모 클래스 생성자 호출시 Base 생성자가 2회 호출되는 문제가 발생한다.
"""

class Unit:
  def __init__(self):
    print("Unit 생성자")
    super().__init__()

class Attack:
  def __init__(self):
    print("Attack 생성자")
    super().__init__()

class AttackUnit(Attack, Unit):
  def __init__(self):
    print("AttackUnit 생성자")
    super().__init__()

class Flyable:
  def __init__(self):
    print("Flyable 생성자")
    super().__init__()

class FlableUnit(Flyable, Unit):
  def __init__(self):
    print("FlableUnit 생성자")
    super().__init__()

class FlyableAttackUnit(AttackUnit, FlableUnit):
  def __init__(self):
    super().__init__()


valkyrie = FlyableAttackUnit()