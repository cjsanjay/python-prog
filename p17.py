#How to remove duplicates from array in place

def removeDuplicates(array):
    i=1
    cur=array[0]
    flag=0
    while i<len(array):
        if array[i]==cur and flag==0:
            swap=i  
            flag=1
        else:
            flag=0
            array[i],array[swap]=array[swap],array[i]
            cur=array[swap]
            swap=swap+1
        i=i+1
    return array                                             
    

array=[1,1,2,4,5,5,6,7,8,9]
print removeDuplicates(array)
