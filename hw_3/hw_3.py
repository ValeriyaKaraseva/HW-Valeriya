#**********
l1 = [1,2,3,4,5,6,7]
l2 = [2,8,9,0,1,11,12]
l3=list(filter(lambda x: x in l1,l2))
print(list(l3))

s1=set(l1)
s2=set(l2)
print(list(s1&s2))

