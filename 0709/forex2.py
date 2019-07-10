'''
Created on 2019. 7. 9.

@author: gd_4
forex2.py : 구구단 출력하기
'''

i, j = 0, 0

for i in range(2, 10, 1) :
    print("%5a단" % i)
    for j in range(1, 10, 1) :
        print("%a X %a = %a" % (i, j, (i * j)))
    print()