class VietnamPackage:
  def detail(self):
    print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")

if __name__ == "__main__": # thailand.py에서 모듈 직접 실행될 경우 실행
  print("vietnam 모듈을 직접 실행")
  print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
  trip_to = VietnamPackage()
  trip_to.detail()
else: # 외부 모듈에서 thailand.py 모듈을 직접 사용할때 실행
  print("vietnam 외부에서 모듈 호출")