### 디지스트의 여러 정보를 쉽게 확인할 수 있는 알림 챗봇을 만들어보자.
디지스트의 여러 정보 (시험 일정, 학사 일정 등)을 모은 후 카카오톡 챗봇을 통해 한번에 확인 할 수 있게 하면 편리할 것이라고 생각했다.
우선적으로는 일정에 관련된 것만 우선적으로 만들어보기로 했다.

### api 서버 준비하기
동적인 응답을 위해서는 api 서버가 필요하다고 생각했다. amazone ec2에서 제한적으로 무료 서버를 사용할 수 있어서 아마존 ec2를 이용해 우분투 서버를 준비했다.
먼저 아마존 aws 콘솔에 접속한다.
[amazone aws](https://ap-northeast-2.console.aws.amazon.com/console/home?region=ap-northeast-2)

![1](https://github.com/chanwoo99/board/blob/master/_posts/2020-03-12-1/1.JPG?raw=true)
솔루션 구축에서 EC2를 선택해 인스턴스를 만들었다.
![1](https://github.com/chanwoo99/board/blob/master/_posts/2020-03-12-1/2.JPG?raw=true)
프리티어로 사용 가능한 ubuntu server 18.04를 선택하고 서버의 성능도 프리티어에서 가능한 옵션들로 선택한다.

인스턴스를 만든 후 서버 접속을 위해 SSH로 ec2 서버에 접속했다.

![1](https://github.com/chanwoo99/board/blob/master/_posts/2020-03-10-1/1.JPG?raw=true)

### flask 설치하기
웹 서버 프레임워크인 flask 파이썬 모듈을 설치한다.

먼저 pip를 설치하고 업데이트한다
```
$ apt install python3-pip
$ pip3 install flask
```
flask의 기본적인 사용법은 flask 사이트를 참고했다.
[flask](https://palletsprojects.com/p/flask/)

이 flask에서 만듬 웹 서버를 외부에서 접속이 가능하게 하려면 ec2 콘솔에서 인바운드 규칙을 추가해 주어야한다.
flask에서 8080포트로 서버를 열었다면, 인바운드 규칙에서도 아래 사진과 같이 추가해 주면
![1](https://github.com/chanwoo99/board/blob/master/_posts/2020-03-12-1/5.JPG?raw=true)
0.0.0.0/0으로 접속시 8080포트를 사용할 수 있다.

### kakaotalk 채널 생성
[kakao](https://center-pf.kakao.com)
카카오톡 채널 관리자센터에 접속해 디지스트 알리미라는 카카오톡 채널을 만들었다.
기본적인 정보를 입력하고 세팅을 한 다음에 챗봇을 만들기 위해 카카오 i 오픈빌더를 사용했다.

### kakaotalk 오픈 빌더
![1](https://github.com/chanwoo99/board/blob/master/_posts/2020-03-12-1/3.JPG?raw=true)
카카오 오픈빌더에는 이런 식으로 구성되어있다.

오픈빌더에 대한 자세한 사용법은
[kakao doc](https://i.kakao.com/docs/getting-started-overview#%EC%98%A4%ED%94%88%EB%B9%8C%EB%8D%94-%EC%86%8C%EA%B0%9C)
링크의 카카오 오픈빌더 도움말을 참고하였다.

스킬에 api 서버 주소를 등록해 발화의 정보를 json 형태로 api 서버로 보낸 후 다시 json 형태로 받아와 정보를 처리 할 수 있었다.

그래서 지금까지 만든 구조는 알고자 하는 일정을 발화를 통해 받아와 api서버에 보내면 api 서버에서 일정의 날짜와 d_day를 다시 전송하는 것이다.
![1](https://github.com/chanwoo99/board/blob/master/_posts/2020-03-12-1/4.JPG?raw=true)
위와 같은 식으로 구성하였다.

### 맺음말
아직은 초기 개발 단계이기 때문에 자세한 개발 과정을 작성하지는 않았다.
또한 기능도 현재 학교의 일정 알림, 제일 가까운 공휴일 알림 만 있는 상태이다.
추가적인 개발로 좀 더 다양한 학교의 정보를 확인할 수 있게 할 생각이다.
지금은 정보를 수동으로 다 입력하고 있지만, selenium을 통해 학교 웹 사이트의 정보를 자동으로 파싱하여 정보를 얻어오도록 수정할 예정이다.

### code
https://github.com/chanwoo99/dgist_chatbot
| 파일 | 역할 |
| ---- | ---- |
| data.py | 학교 정보를 작성한 데이터 |
| main.py | 서버 실행 파일 |
| timemodule.py | 일정 정보에서 시간을 다룰때 사용할 모듈 |
