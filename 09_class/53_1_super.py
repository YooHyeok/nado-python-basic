""" 
[super]
"""

# 지상 유닛 - 속도 speed 멤버 추가
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 건물
class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    Unit.__init__(self, name, hp, 0)
    super().__init__(name, hp, 0) # super()를 통해 부모 클래스(Unit)을 초기화 할 경우 self는 생략한다.
    self.location = location


# Super 문제점 - 두개이상의 부모클래스를 다중 상속 받을 경우 가장 처음 상속받는 클래스에 대해서만 init 함수가 호출된다.
class Unit:
  def __init__(self):
    print("Unit 생성자")

class Flyable:
  def __init__(self):
    print("Flyable 생성자")

class FlableUnit(Unit, Flyable):
  def __init__(self):
    super().__init__()

dropship = FlableUnit() # Unit 생성자 출력

class Unit:
  def __init__(self):
    print("Unit 생성자")

class Flyable:
  def __init__(self):
    print("Flyable 생성자")

class FlableUnit(Flyable, Unit):
  def __init__(self):
    super().__init__()

dropship = FlableUnit() # Flyable 생성자 출력

class FlableUnit(Flyable, Unit):
  def __init__(self):
    Flyable.__init__(self)
    Unit.__init__(self)

dropship = FlableUnit() # Flyable 생성자, Unit 생성자 출력
