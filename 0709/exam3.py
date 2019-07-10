'''
Created on 2019. 7. 10.

@author: gd_4
'''

name = {"한국" : "서울", "중국" : "베이징", "일본" : "도쿄", "영국" : "런던", "독일" : "베를린"}

name.pop("일본") # 삭제 메소드

while True :
    inname = input(str(list(name.keys())) + "나라를 입력하세요. 또는 끝 또는 삭제를 입력하세요")
    if inname in name : # 입력받은 값이 foods에 존재?
        print("<%s> 의 수도는 <%s> 입니다." % (inname,name.get(inname)))
   
    elif inname == "끝" :
        for i in name.keys() :
            print("%s => %s" % (i, name[i]), end=",")
        break
    
    elif inname == "삭제" :
        dl = input("삭제하고 싶은 나라를 입력하세요")
        name.pop(dl)
            
    else :
        print("그런 나라는 등록되 있지 않습니다.")
        yn = input("나라를 등록 하시겠습니까? (y/n)")     
       
        if yn == 'y' :
            city = input("나라의 수도를 입력하세요")
            name[inname] = city
       
        elif yn == "n" :
            continue