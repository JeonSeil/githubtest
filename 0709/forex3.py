'''
Created on 2019. 7. 9.

@author: gd_4
'''
i, j = 0, 0

for i in range(2, 10, 1) :
    print("%d단%19s" % (i," "),end="")
print()
for j in range(2, 10, 1) :
    for i in range(2, 10, 1) :
        print("%2d X%2d =%3d" % (i,j,(i*j)),end="")
    print()