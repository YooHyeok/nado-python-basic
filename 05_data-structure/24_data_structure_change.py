# 자료구조의 변경

menu = {"커피", "우유", "주스"} # 중괄호는 딕셔너리(사전)
print(menu, type(menu)) # {...} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # [...] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # (...) <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {...} <class 'set'>