from pyfirmata import Arduino,util

DELAY = 1
MIN = 5
MAX = 175
MID = 90

#핀 모드설정
board = Arduino('COM8')
servo = board.get_pin('d:8:s') #8번핀을 서보모터 신호선으로 설정

#모터 작동 함수 작성 
def move_servo(v):
    servo.write(v)
    board.pass_time(DELAY)


print("start")
move_servo(MIN)
move_servo(MAX)
move_servo(MID)
print("fin")

board.exit()



