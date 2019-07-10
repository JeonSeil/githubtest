'''
Created on 2019. 7. 10.

@author: gd_4
'''

foods = {"떡볶이" : "오뎅", "짜장면" : "단무지", "라면" : "김치", "피자" : "피클",
         "맥주" : "치킨", "삼겹살" : "상추"}

for i in foods.keys() :
    print("%s=>%s" % (i,foods[i]))
    #print(i, "=>", foods[i])

while True :
    myfood = input(str(list(foods.keys())) + "중 좋아하는 음식은?")
    if myfood in foods : # 입력받은 값이 foods에 존재?
        print("<%s> 궁합 음식은 <%s> 입니다." % (myfood,foods.get(myfood)))
    elif myfood == "끝" :
        for i in foods.keys() :
            print("%s => %s" % (i, foods[i]), end=",")
        break
    else :
        print("그런 음식은 등록되어 있지 않습니다.")
        yn = input("좋아하는 음식으로 등록 하시겠습니까? (y/n)")
        
        if yn == 'y' :
            f = input("궁합음식을 입력하세요")
            foods[myfood] = f 