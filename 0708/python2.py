'''
Created on 2019. 7. 8.

@author: gd_4
input() 함수, print() 함수
'''

a = int(input("값을 입력하세요"))  # input() 함수는 기본적으로 문자열 입력받음.
b = int(input("값을 입력하세요"))

result = a+b
print(a, "+", b, "=", result)   # , 를 이용하여 여러개의 값을 출력함
result = a-b
print(a, "-", b, "=", result)

print("%d" % 123)   # 123
print("%5d" % 123)  # %5d : 5자리 확보
print("%05d" % 123) # %05d : 5자리 확보 후 0으로 채우기

print("%f" % 123.45) # 실수 출력
print("%7.1f" % 123.45) # %7.1f 소수점 1자리 까지 
print("%7.3f" % 123.45) # %7.3f 소수점 3자리까지

print("%s" % "Python") # 문자출력
print("%10s" % "Python") # "10s 출력하고 10자리 확보

print("%d / %d = %5.1f" % (100, 200, 0.5))

#format 함수를 이용하여 다양한 서식 지정이 가능함
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
print("{2:d} {1:d} {0:d}".format(100, 200, 100))

# print 함수는 자바의 println 함수와 동일. 그럼 자바의 print 함수는?
print("안녕하세요", end="")
print("홍길동님")