mylist = [1,2,3,7,1,5,9,3,4,7,2,4,9,6]
def duplicate():
    mylist.sort()
    for i in range(1,13):
        if mylist[i]==mylist[i-1]:
            print(mylist[i])
duplicate();
