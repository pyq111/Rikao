import random
list2=[]
list1=[random.randrange(100)for i in range(10)]
print(list1)
list2=list1.copy()
print("第二个列表:",list2)
list2.reverse()
print("反向输出:",list2
