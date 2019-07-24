def group(mylist,size):
    list1=[]
    list2=[]
    i=0
    while i<len(mylist):
        if len(list2)<size:
           list2.append(mylist[i])
           i+=1
        else:
           list1.append(list2)
           list2=[]
    list1.append(list2)
    return list1
print(group([0,1,2,3,4,5,6,7,8,9],3))
