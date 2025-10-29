""" 
[__init__.py와 __all__ 변수]

__init__.py 파일을 생성할경우 패키지 초기화 파일로 인식된다.
해당 파일 내에서 __all__ 변수에는 __init__.py와 동일한 패키지에 존재하는 모듈 파일 내의 from~import 구문에서 어떤 것을 가져올지 미리 정해주는 리스트를 정의한다.

에를들어 아래 코드를 정의했다고 가정해보자.

from travel import * 
trip_to = vietnam.VietnamPackage()

위 코드에서는 오류가 발생한다.  

travel 패키지를 불러온 뒤 travle 패키지의 vietnam 모듈에 접근하기 위해서는 
travel 패키지 안에 포함된 모든 것들 중 import 되기 원하는 대상에 대한 공개 범위를 설정해줘야 한다.
이때 앞서 말했듯 from~import 구문과 동일한 패키지 하위에 __init__.py라는 패키지 초기화 파일을 생성한 후, __all__ 변수를 정의하여 가져올 대상을 정의해야 한다.
"""

__all__ = ["vietnam", "thailand"] # vietnam, thailand 모듈을 불러온다.