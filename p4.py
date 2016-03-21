

array=[1,2,3,8,5]

def search(val,array,start):
    if start<len(array):
        for i in range(start,len(array)):
            if array[i]==val:
                return i            
    else:
        return -1    
    return -1    
    
def getArray(array):    
    i=0
    cur=0
    while i<len(array)-2:
        val=pow(array[i],array[i+1])
        pos=search(val,array,i+2)
        if pos!=-1:           
            array[cur]=array[i]
            array[cur+1]=array[i+1]        
            array[cur+2]=array[pos]                      
            for j in range(cur+3,len(array)):                
                array[j]=0
            return array              
            i=cur
        else:
            array[i]=0                     
        i=i+1               
    return array

print getArray(array)                
