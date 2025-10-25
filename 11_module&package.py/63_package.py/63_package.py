""" 
[패키지]
 """

# import 구문에는 항상 모듈 혹은 패키지만 참조 가능, class는 불가
import travel.thailand # 패키지 하위의 모듈을 참조할때는 무조건 . 도트로 접근해야만 한다.
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from~import 구문에는 모듈, 패키지, 클래스, 함수 모두 import 가능
from travel.vietnam import VietnamPackage
trip_to = VietnamPackage()
trip_to.detail()

# package로부터 vietnam 임포트
from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()