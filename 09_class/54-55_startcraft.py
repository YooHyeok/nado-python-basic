
""" 
[스타크래프트 - 전반전]
"""

# 지상 유닛 - 속도 speed 멤버 추가
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print("{0} 유닛이 생성되었습니다.".format(name))

  def move(self, location):
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, self.damage))
    self.hp -= damage
    print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴 되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit): # 속도 speed 멤버 추가
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage
  
  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
  
# ====================================================================================================================

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


# 공중 공격 유닛 클래스 - 다중상속은, 로 구분
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, 0, damage) # 속도 speed 멤버 추가
    Flyable.__init__(self, flying_speed)
  
  def move(self, location):
    self.fly(self.name, location)

# --------------------------------------------------------------------------------------------------------------------

# [마린]
class Marine(AttackUnit):
  steampack_developed = False
  def __init__(self):
    AttackUnit.__init__(self, "마린", 40, 1, 5)

  # 스팀팩: 일정 시간 동안 이동 및 공격 속도 증가. 체력 10 감소
  def steampack(self):
    if Marine.steampack_developed == False:
      return
    if self.hp > 10: 
      self.hp -= 10
      print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
      return
    print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# [탱크]
class Tank(AttackUnit):
  seize_developed = False # 시즈모드는 업그레이드 하게 되면 모든 탱크에 동일하게 적용된다고 가정하고, 클래스 바로 밑에 선언
  def __init__(self):
    AttackUnit.__init__(self, "탱크", 150, 1, 35)
    self.seize_mode = False

  # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
  def set_seize_mode(self):
    # 시즈모드 개발여부 - 개발되지않았다면 시즈모드 통제 불가
    if Tank.seize_developed == False:
      return
    # 시즈 모드가 아닐 때 → 시즈모드 ON
    if self.seize_mode == False: 
      print("{0} : 시즈모드로 전환합니다.".format(self.name))
      self.seize_mode = True
      self.damage *= 2
      return
    # 시즈 모드 일 때 → 시즈모드 OFF
    if self.seize_mode == True: 
      print("{0} : 시즈모드를 해제합니다.".format(self.name))
      self.seize_mode = False
      self.damage /= 2
      return


# [레이스]
class Wraith(FlyableAttackUnit):
  clocked_developed = False
  def __init__(self):
    FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
    self.clocked = False # 클로킹 모드(해제 상태)

  def clocking(self):
    if self.clocked_developed == False:
      return
      
    if self.clocked == False:
      print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
      self.clocked = True
      return

    if self.clocked == True:
      print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
      self.clocked = False
      return


# --------------------------------------------------------------------------------------------------------------------

def game_start():
  print("[알림] 새로운 게임을 시작합니다.")

def game_over():
  print("Player : gg") # good game
  print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()
print()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 ㅅㅅㅅ생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

print()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
print()

# 전군 이동
for unit in attack_units:
  unit.move("1시")
print()

# 탱크 시즈모드 개발
Marine.steampack_developed = True
Tank.seize_developed = True
Wraith.clocked_developed = True

print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
print()

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
  if isinstance(unit, Marine) : # isinstance(obj): obj가 어떤 클래스의 인스턴스인지 확인
    unit.steampack()
  elif isinstance(unit, Tank) :
    unit.set_seize_mode()
  elif isinstance(unit, Wraith) :
    unit.clocking()
print()


# 전군 공격
for unit in attack_units:
  unit.attack("1시")
print()

from random import *
# 전군 피해
for unit in attack_units:
  unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)
print()

# 게임 종료
if sum(unit.hp for unit in attack_units) == 0:
  game_over()