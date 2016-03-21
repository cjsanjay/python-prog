
def  getIntegerComplement1( n):
    print ~n
    print bin(~n).split('b')[1]
    binary=bin(n).split('b')[1]
    print binary
    ans=""
    for each_b in binary:
        if each_b=="0":
            ans=ans+"1"
        else:
            ans=ans+"0"
    print ans        
    print int(ans,2)
    
def  getIntegerComplement( n):
    b=1
    ans=""
    if n==0:
        return 1
    while n-b>=0:
        if n & b ==b:
            ans="0"+ans
        else:
            ans="1"+ans
        b=b<<1     
    print bin(n).split('b')[1]    
    print ans        
    print int(ans,2)     

getIntegerComplement(300)                
