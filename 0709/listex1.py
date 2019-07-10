'''
Created on 2019. 7. 10.

@author: gd_4
listex1.py : 리스트예제
 리스트, 딕셔너리(Map), 튜플
'''

a = [0, 0, 0, 0]
hap = 0

for i in range(0, 4) :
    a[i] = int(input(str(i+1) + "번째 값 :"))
    hap += a[i]
print("합계", hap)