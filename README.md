# KAIST WEB ERP Auto program

학교에서 ERP 노가다하다가 빡쳐서 1시간만에 만든 프로그램입니다.

ERP 행정처리 할 때 귀찮은 부분을 자동으로 채워줍니다.

## 사용방법

1. 위에 "Code">"Download ZIP"을 클릭하여 ip 압축파일을 받은 후 풀어줍니다.
1. 푼 압축파일의 KAIST_WEB_ERP_Auto-main 폴더에서 "여기에 필요한 내용을 용도에 맞게 입력하세요.txt"의 변수 내용을 필요에 따라 바꿉니다. (Portal ID와 PW는 필수로 입력)
1. "KAIST_WEB_ERP_Auto.exe"를 실행하면 자동으로 크롬 팝업이 뜨면서 ERP가 진행이 됩니다.
1. `품명`과 `예산배분`만 빼놓고 모두 자동으로 채워줍니다. 이 부분은 행정처리 할 때마다 달라져서 직접 입력해야 합니다.
1. 비어있는 부분이 없는 지 체크하고 `승인요청` 하시면 됩니다.


## 실행해도 Chrome이 안 켜질 때

1. [이 블로그](https://blog.naver.com/song_sec/221752226329)를 참고해서 자신의 크롬 버전에 맞는 chromedriver를 다운로드 받은 후, KAIST_WEB_ERP_Auto 폴더에 기존의 chromdriver.exe를 지우고 바꿔치기합니다.


## 수정하고 싶을 때

1. [Anaconda](https://www.anaconda.com/)를 다운로드 받습니다.
1. `pip install selenium`을 통해 `selenium`을 설치합니다.
1. "KAIST_WEB_ERP_Auto.py" 파일을 원하는 대로 바꿔서 실행합니다.