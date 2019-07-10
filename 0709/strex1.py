'''
Created on 2019. 7. 9.

@author: gd_4

strex1.py : 문자열 값 출력하기

문자열은 문자의 배열
'''

print("안녕하세요")
print("안녕하세요" [0]) # 앞 0부터
print("안녕하세요" [4], "안녕하세요" [-1]) # 뒤 -1부터
print("안녕하세요" [3], "안녕하세요" [-2])
print("안녕하세요" [1:3]) # 1번인덱스부터 2번인덱스 까지. 3번인덱스 앞까지
print("안녕하세요" [:2]) # 0번인덱스부터 2번인덱스 까지. 3번인덱스 앞까지
print("안녕하세요" [2:], "안녕하세요" [:2]) # 2번인덱스부터 끝문자까지

s = "안녕하세요"
print(type(s))

num = 10
print(type(num))

num = 10.5
print(type(num))

print("s 문자열의 길이:", len(s))
print("len(s) 의 자료형 :", type(len(s)))

#배열 : List 자료형
arr = [10, 20, 30, 40, 50, 60, 70]
print(type(arr))

print(arr[0])
print(arr[:1])

# 30부터 50까지의 값을 출력
print(arr [2:5])
print(arr [::2])
print(arr [::-2])
print(arr [::-1])