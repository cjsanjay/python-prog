"""How to find sub array with maximum sum in an array of positive and negative number
"""


def maxSum(array,i,sum1):
    "DP O(n^2)"
    if i==len(array):
        return sum1
    else:
        return max(maxSum(array,i+1,sum1+array[i]),maxSum(array,i+1,0),sum1)    
        
def maxSum1(array):
    "kadane algorithm keep two variable final_max and temp_max update final_max when temp_max > final_max if temp_max drops <0 than make it zero as its smart to start a new range now on O(n)"
    print array
    final_max=0
    temp_max=0
    i=0
    range_start=0
    range_end=0
    while i<len(array):
        if temp_max+array[i]<0:
            temp_max=0
            range_start=i+1
        else:
            temp_max=temp_max+array[i]
            if final_max<temp_max:
                final_max=temp_max    
                range_end=i
        i=i+1                 
    return final_max,range_start,range_end  
    
def maxProduct(array):
    final_max=1
    temp_max=1
    i=0
    while i<len(array):
        if temp_max*array[i]==0 and temp_max<0:
            temp_max=1
        else:
            temp_max=temp_max*array[i]
            if final_max<temp_max:
                final_max=temp_max    
        i=i+1                       
    return final_max
array=[-2,1,-3,4,-1,2,1,-5,4]
print maxProduct(array)
