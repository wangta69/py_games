# 프로그램설치 및 환경구성



## 아나콘다 세팅
[다운로드](https://www.anaconda.com/products/individual) <br>
위의 사이트에서 하단으로 스크롤 하면 링크가 나온다. <br>
본인의 시스템에 맞는 프로그램을 다운로드한다.
![alt 아나콘다1](../assets/images/docs/anaconda1.png)

## 파이썬 세팅
[다운로드](https://www.python.org/downloads/)
아나콘다만 설치해도..

## PyCharm(IDE) 설치
[다운로드](https://www.jetbrains.com/ko-kr/pycharm/download/)

Community는 무료이며 이것을 이용해도 개발에는 부족함이 없다.

![alt 파이참1](../assets/images/docs/pycharm1.png)

### 화면구성
- 기본화면 구성
![alt 파이참2](../assets/images/docs/pycharm2.png)

### 환결설정
- File > Settings....

![alt 파이참3](../assets/images/docs/pycharm3.png)

- Project > Python Interpreter : 세팅아이콘 > Add

![alt 파이참4](../assets/images/docs/pycharm4.png)

- Conda Environment > New Environment
![alt 파이참5](../assets/images/docs/pycharm5.png)

세팅완료!!

### 패키지 설치

- PyCharm 하단의 "Terminal" 클릭
- Command Line에 pip install [패키기명]

![alt 파이참6](../assets/images/docs/pycharm6.png)


### 패키지 설치 > pygame
- 아래처럼 입력하면 pygame 패키지가 설치됩니다.
```
pip install pygame
```