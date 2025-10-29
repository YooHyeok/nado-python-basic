import inspect
import random
print(inspect.getfile(random)) # random 모듈의 위치를 확인 : C:\Python313\Lib\random.py

from travel import *
print(inspect.getfile(thailand)) # travel 패키지의 thailand 모듈의 위치를 확인 : c:\Users\dq\diquest\study\inflearn\nado-python-basic\11_module&package.py\66_package-module-location.py\travel\thailand.py

""" 
[패키지, 모듈 위치]
- inspect: 파이썬 객체를 조사(inspection)하기 위한 표준 라이브러리 모듈이다.  
  함수, 클래스, 메서드, 모듈 등 런타임(실행 중)에도 객체의 내부 구조를 알아낼 수 있다.
- inspect.getfile(모듈): 모듈의 위치를 확인

1. travel 패키지 PYTHONPATH 환경변수에 지정된 디렉토리로 이동 - 실행
2. 현재 패키지의 travel 패키지 이름 변경 - 실행

c:\{파이썬 경로}\Lib\
위 디렉토리 경로는 PYTHONPATH 환경변수에 지정된 디렉토리이다.  
해당 위치에 모듈이 포함된 패키지를 구성할 경우. 해당 모듈을 읽게된다.  
우선순의는 현재 실행한 모듈이 위치한 패키지가 먼저이고, 현재 모듈이 위치한 패키지에 없다면 해당 위치에서 읽는다.  
 """