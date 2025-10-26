
from random import * # random 모듈 안의 모든것들을 사용한다.
from travel import * # travel 패키지의 모든것을 허용 - 패키지 안에 포함된 모든 것들 중에 import 되기 원하는 대상에 대한 공개 범위를 설정해줘야 한다.
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()