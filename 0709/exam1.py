'''
Created on 2019. 7. 9.

@author: gd_4

exam1.py : 문제
    금액을 입력받아 필요한 동전의 갯수 출력하기
    단 동전은 500, 100, 50, 10, 1 종류가 있다
    필요한 동전의 갯수는 최소로 한다
'''
coin = [500, 100, 50, 10, 1]

money = int(input("금액을 입력하세요"))

result0 = money // coin[0]
money = money % coin[0]

result1 = money // coin[1]
money = money % coin[1]

result2 = money // coin[2]
money = money % coin[2]

result3 = money // coin[3]
money = money % coin[3]

result4 = money // coin[4]

print("필요한 500원 동전은", result0, "개")
print("필요한 100원 동전은", result1, "개")
print("필요한 50원 동전은", result2, "개")
print("필요한 10원 동전은", result3, "개")
print("필요한 1원 동전은", result4, "개")
