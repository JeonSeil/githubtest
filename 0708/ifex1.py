'''
Created on 2019. 7. 8.

@author: gd_4
ifex1.pv : if, else 예제
'''
score = int(input("점수를 입력하세요(0~100):"))
if score >= 90 :
    print("A학점")
else :
    if score >= 80 :
        print("B학점")
    else :
        if score >= 70 :
            print("C학점")
        else :
            if score >= 60 :
                print("D학점")
            else :
                print("F학점")
    
print("if elif 구문")
if score >= 90 :
    print("a학점")
elif score >= 80 :
    print("b학점")
elif score >= 70 :
    print("c학점")
elif score >= 60 :
    print("d학점")
else :
    print("f학점")
    