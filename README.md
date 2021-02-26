# Arduino example 7
Tutorial 7.Servo Motor\
servo motor의 각도가 5도 → 175도 → 90도 순서로 바뀌도록 제작

## circuit
servo motor : digital 8pin\
![image](https://user-images.githubusercontent.com/79436159/109196147-afc06a00-77de-11eb-843c-20868af79ca1.png)

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

```
DELAY = 1
MIN = 5
MAX = 175
MID = 90
```
지연시키기위한 변수 DELAY변수를 1초로 정의하고 \
최소각도값 변수인 MIN 변수에는 5를, 최대각도값 변수인 MAX 변수엔 175도를, \
중간각도값 변수인 MID 변수에는 90을 임의로 정의함

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

 ```led = board.get_pin('d:8:s') ```\
  -> 8번 핀을 digital신호 신호핀으로 설정\
  신호핀으로 설정하면 sevor motor에 신호를 주는 핀으로 설정됨
  
```
def move_servo(v):
  servo.write(v)
  board.pass_time(DELAY)
```
모터를 움직이게 하는 함수 작성\
원하는 각도를 입력으로 주고 DELAY변수만큼 지연시킴

```
print("start")
move_servo(MIN)
move_servo(MAX)
move_servo(MID)
print("fin")
```
시작할때 문자열 "start"를 출력하고 각도를 변화시킨후 문자열 "fin"을 출력시킴

```board.exit()``` \
동작을 종료시킴
