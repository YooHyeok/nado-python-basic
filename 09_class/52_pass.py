""" 
[pass]
실행할 코드가 없음 의미한다.
함수나 클래스의 구현을 미룰때 사용. 
python에서는 빈 블록을 허용하지 않으므로 함수, 매소드, 클래스를 비워둘 경우 오류가 발생한다.
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
    pass # 비워두지 않고 pass

# 서플라이 디폿: 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
  print("[알림] 새로운 게임을 시작합니다.")

def game_over():
  pass # 비워두지 않고 pass

game_start()
game_over()
