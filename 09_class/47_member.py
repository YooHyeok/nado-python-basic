""" 
[클래스-멤버변수]  
클래스 내에 선언된 변수이다.  
__init__() 생성자 함수 선언시 매개변수로 선언하고 함수 내에서 초기화해준다.
외부에서는 `인스턴스변수명.멤버변수명` 형태로 생성된 인스턴스 변수를 통해 접근 가능하다.
클래스 외부에서 원하는 변수 확장(멤버 추가 및 값 할당)이 가능하며, 확장 한 객체에 대해서만 적용된다.
"""
class Unit:

  # 생성자 __init__():
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # 외부에서 멤버 추가 및 할당

if wraith2.clocking == True:
  print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

if wraith1.clocking == True:
  print("{0} 는 현재 클로킹 상태입니다.".format(wraith1.name))