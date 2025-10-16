""" 
[Pickle]
프로그램상에서 사용하고 있는 데이터(자료구조)를 파일 형태로 저장한다.
"""
import pickle
profile_file = open("profile.pickle", "wb") # wb: w는 쓰기, b는 바이너리를 의미(픽클에서는 바이너리를 정의해야한다.)
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 정보를 profile_file 파일에 쓰기
profile_file.close()

profile_file = open("profile.pickle", "rb") # rb: r은 읽기, b는 바이너리를 의미(픽클에서는 바이너리를 정의해야한다.)
profile = pickle.load(profile_file) # 읽어온 파일 정보(내용)을 실제로 불러오기
print(profile)