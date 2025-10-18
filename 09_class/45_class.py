# 마린: 공격 유닛, 군인. 총을 쏠 수 있음.
name = "마린" # 유닛 이름
hp = 40 # 유닛 체력
damage = 5 # 유닛 공격력
print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크: 공격 유닛, 탱크. 포를 쏠 수 있으며, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# 공격 함수
def attack(name, location, damage):
  print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 탱크를 새로 생성
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35
attack(tank2_name, "1시", tank2_damage)

""" 
[클래스]
위와 같이 탱크 정보 혹은 마린 정보를 새로 생성해야 할 경우, 생성 할 양이 많다면 반복되는 코드가 많이 발생하게 된다.
이때 해당 정보들을 객체로 관리할 수 있는 클래스를 사용하면 유용하다.
"""

# 유닛 클래스 정의
class Unit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 정의한 클래스 사용
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)