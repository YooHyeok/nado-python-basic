""" 
[메소드]
"""

# 공격 유닛
class AttackUnit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
  
  # 공격 메소드
  def attack(self, location): # self: 자기 자신을 의미하며, 메소드의 첫번째 매개변수로 항상 받는다.
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

  # 공격 받은 메소드
  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    self.hp -= damage # 체력 감소
    print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃: 공격 유닛, 화염 방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 2번 받음
firebat1.damaged(25) # 체력 25(50 - 25)
firebat1.damaged(25) # 체력 0(25 - 25)