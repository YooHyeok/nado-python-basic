""" 
[모듈]
함수정의나 클래스 등의 프로그래밍 문장들을 담고 있는 파일을 모듈이라고 한다.

파이썬 모듈의 확장자는 .py이다.
모듈 파일 이름의 앞에는 숫자가 들어올 수 없다.
모듈파일의 중간에는 하이픈(-)이 들어올 수 없다.
"""

import theater_module
theater_module.price(3) # 10000 * 3 = 30000
theater_module.price_morning(4) # 6000 * 4 = 24000
theater_module.price_soldier(5) # 4000 * 5 = 20000

# 별칭 부여
import theater_module as mv # mv라는 이름의 별칭을 부여한다.
mv.price(3) # 10000 * 3 = 30000
mv.price_morning(4) # 6000 * 4 = 24000
mv.price_soldier(5) # 4000 * 5 = 20000

# from~import 구문 - 접근없이 직접 접근하여 사용 가능, *은 모든것을 참조
try:
  # from theater_module import * 
  from theater_module import price, price_morning
  price(3) # 10000 * 3 = 30000
  price_morning(4) # 6000 * 4 = 24000
  price_soldier(5) # 4000 * 5 = 20000
except NameError as e:
  print("오류 발생 - 예외 타입:", type(e).__name__)
  from theater_module import price_soldier
  price_soldier(5) # 4000 * 5 = 20000


# from~import 구문 - 필요한 함수만 import
from theater_module import  Hi
hi = Hi()
