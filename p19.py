"""Given two sorted integer arrays A and B, merge B into A as one sorted array. You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively. This is another intermediate array coding question, its not as simple as previous one but neither very difficult.
"""


def mergeArray(array1,array2):   
    #Assuming array1 has sufficient space for array2 that means size of array1 is len(array1)+len(array2). So using that extra space for palcing values in last order. Hence we need to start from end for both arrays and place values.  
    i=len(array1)-len(array2)-1
    j=len(array2)-1
    place=len(array1)-1
    while i>=0 and j>=0:
        if array1[i]>array2[j]:
            array1[place]=array1[i]
            place=place-1
            i=i-1
        else:
            array1[place]=array2[j]
            place=place-1
            j=j-1       
    return array1                           

array=[1,3,5,7,9,11,0,0,0,0,0]
array2=[2,4,6,8,10]
print mergeArray(array,array2)
