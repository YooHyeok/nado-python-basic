""" 
[클래스-생상자]  
__init__()은 생성자이다.  
인스턴스 즉, 객체가 만들어질 때 자동으로 호출되는 부분이다.  
생성자의 기본 매개변수 첫번째 인자로 self를 받게 된다.  
인스턴스를 생성할 때 생성자 매개변수 중 self를 제외하고 동일한 매개변수를 전달해야 한다.  
"""
class Unit:

  # 생성자 __init__():
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # __init__(self, name, hp, damage)에 self를 제외하고 순차적으로 name = "마린", hp = 40, damage = 5 가 전달된다.
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)