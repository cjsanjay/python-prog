#Rearrange array with alternate positive and negative values

def reArrange(input1):
    print input1
    place=-1
    i=0
    while i<len(input1):        
        if input1[i]<0:
            place=place+1
            temp=input1[i]
            input1[i]=input1[place]
            input1[place]=temp
        i=i+1             
    neg=0
    pos=place+1   
    print input1    
    while neg<len(input1) and neg<pos and input1[neg]<0:
        temp=input1[neg]
        input1[neg]=input1[pos]
        input1[pos]=temp      
        neg=neg+2
        pos=pos+1
    return input1    

input1=[1, 2, 3, -4, -1, 4]
print reArrange(input1)
