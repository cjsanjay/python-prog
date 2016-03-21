#Max sub array sum

array=[-2, 5, -1, 7, -3]

max_array=[]
result_array=[]
memo={}
def findMax(array,current,cur_sum1,max_array):
    if str(current)+str(cur_sum1) in memo:
        return memo[str(current)+str(cur_sum1)],max_array
    else:        
        if current==len(array):        
            memo[str(current)+str(cur_sum1)]=cur_sum1
            return cur_sum1,max_array
        else:    
            val1,max_array=findMax(array,current+1,cur_sum1+array[current],max_array)
            val2,max_array=findMax(array,current+1,cur_sum1,max_array)            
            if val1>val2:
                memo[str(current)+str(cur_sum1)]=val1
                if current not in max_array:
                    max_array.append(current)       
                    result_array.append(array[current])                         
                return val1,max_array
            else:
                memo[str(current)+str(cur_sum1)]=val2                 
                return val2,max_array

val,max_array=findMax(array,0,0,max_array)              

print val
print max_array
print result_array

        

