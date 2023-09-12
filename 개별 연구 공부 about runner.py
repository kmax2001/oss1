
O #directories 부분

ㄱ. 코드 설명
- task_path에 runner.py의 경로 중 디렉토리 부분을 대입
- home_path에 /home/younghokim/raisimLib 입력

ㄴ. 배경 지식
- os.path.dirname(): 경로 중 디렉토리명만 얻기
- 예)os.path.dirname("C:/Python35/Scripts/pip.exe") -> "C:/Python35/Scripts"
- os.path.realpath(__file__): __file__은 파일 이름을 문자열로 나타내고, os.path.realpath는 그 파일의 
경로를 나타냄

-
- 참조: https://velog.io/@devmin/%ED%8C%8C%EC%9D%B4%EC%8D%AC-import%EA%B0%80-module%EA%B3%BC-package-%EB%A5%BC-%EC%B0%BE%EC%95%84%EA%B0%80%EB%8A%94-%EA%B2%BD%EB%A1%9C

