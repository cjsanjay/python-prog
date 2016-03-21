#Find Sub array with sub set having sum equal to zero

def findSubSet(array): 
    #using sorting...sort and find middle increment pos or neg pointer until zero is found
    array=sorted(array)
    sum1=array[0]
    i=0
    while i<len(array) and array[i]<=0:
        if array[i]==0:
            return True
        i=i+1
    if i==len(array):
        return False        
    print array    
    pos=i+1
    neg=i-1
    sum1=array[i]
    while neg>=0 and pos<len(array):
        if sum1+array[pos]+array[neg]<0:
            pos=pos+1
        else:
            if sum1+array[pos]+array[neg]>0:
                neg=neg-1
            else:
                return True                 
    return False    
                     
def findSubSet1(array):
    #using window method since sub array start from 0 and shift towards getting sum or zero
    print array
    i=1
    start=0
    cur_sum=array[0]
    el=1
    while i< len(array):
        while cur_sum+array[i]>0 and start<i:        
            cur_sum=cur_sum-array[start]
            el=el-1
            start=start+1
        cur_sum=cur_sum+array[i]
        el=el+1    
        if cur_sum==0 and el!=0:
            print start,i
            return True
        i=i+1  
    return False                  

array=[4, 1, -4, 1, 1]
if findSubSet1(array):
    print "Yes"
else:
    print "No"    
