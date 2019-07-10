'''
Created on 2019. 7. 10.

@author: gd_4
whileex2.py : 랜덤 함수를 사용하여 숫자 맞추기
    컴퓨터가 1부터 100까지의 임의의 수를 저장하고, 화면에 숫자를 입력받아
컴퓨터가 저장한 수 를 맞추기. 입력된 수 가 저장된 수 보다 크면 작은 수 를 입력하세요. 메세지를 출력
입력된 수 가 저장된 수 보다 작으면  더 큰 수 를 입력하세요. 메세지를 출력하기
저장된 수 와 입력된 수 가 같은 경우, 입력 건수를 화면에 출력하고 프로그램 종료.ㅣ
'''

import random

rnum = random.randrange(0, 100)
print("저장된 수 : %d" %rnum)
i = 0
while True :
    a = int(input("숫자를 입력하세요(종료:0) : "))
    if a == 0 :
        break
    if rnum > a :
        i = i + 1
        print("큰 수 를 입력하세요")
    elif rnum < a :
        i = i + 1
        print("작은 수 를 입력하세요")
    elif rnum == a :
        print("정답입니다.", i, "번만에 맞췄습니다.")
        break
print("프로그램 종료")