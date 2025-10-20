""" 
[메소드 오버로딩]
부모 클래스에서 정의한 메소드가 아닌 자식 클래스에서 정의한 메소드를 쓰고 싶을 때  
메소드를 새롭게 정의해서 사용하는 것을 말한다.  
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

class AttackUnit(Unit): # 속도 speed 멤버 추가
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage
  
  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, self.damage))
    self.hp -= damage
    print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴 되었습니다.".format(self.name))

  
# 날 수 있는 기능을 가진 클래스
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 유닛 클래스
class FlyableUnit(Unit, Flyable):
  def __init__(self, name, hp, flying_speed):
    Unit.__init__(self, name, hp, 0) # 속도 speed 멤버 추가
    Flyable.__init__(self, flying_speed)

# 드랍쉽: 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
dropship = FlyableUnit("드랍쉽", 200, 5)
dropship.fly(dropship.name, "2시")

# 공중 공격 유닛 클래스 - 다중상속은, 로 구분
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, 0, damage) # 속도 speed 멤버 추가
    Flyable.__init__(self, flying_speed)
  
  def move(self, location):
    print("[공중 유닛 이동]")
    self.fly(self.name, location)

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
vulture.move("11시")

# 배틀 크루저: 공중 유닛, 체력과 공격력 모두 최강
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # move 오버라이딩 후 location만 전달