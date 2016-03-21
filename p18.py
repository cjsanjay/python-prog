# How to remove a given element from array


def removeE(array,num):   
    end=len(array)-1
    i=0
    count=0
    while i<len(array):
        if array[i]==num:
            while array[end]==num and end>i:
                count=count+1
                end=end-1                
            array[end],array[i]=array[i],array[end]            
        count=count+1        
        i=i+1    
    print count    
    return array[:end],count    

array=[1,2,4,5,6,7,8,9,5,5]
print removeE(array,5)
