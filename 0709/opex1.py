'''
Created on 2019. 7. 9.

두개의 정수를 입력받아 +, -, *, /, % 연산 후의 결과를 출력하기
                
                // : 두수의 몫을 정수로 계산
                ** : 제곱
                
문자열 연결 : +, * 연산 사용
@author: gd_4
'''
num1 = int(input("첫번째 정수를 입력하세요"));
num2 = int(input("두번째 정수를 입력하세요"));

print(num1, "+", num2, "=",(num1 + num2))
print(num1, "-", num2, "=",(num1 - num2))
print(num1, "*", num2, "=",(num1 * num2))
print(num1, "**", num2, "=",(num1 ** num2))
print(num1, "/", num2, "=",(num1 / num2))
print(num1, "//", num2, "=",(num1 // num2))
print(num1, "%", num2, "=",(num1 % num2))

print("a" + "b" + "c")
print("abc" * 3)
