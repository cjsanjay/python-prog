#Count all one in the bit representation

data=int(21)

count=0
while data-1>=0:   
    if data & 1 ==1:
        count=count+1
    data=data>>1

print count                
