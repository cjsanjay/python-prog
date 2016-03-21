def braces(string1):
    count=0
    cur_element=""
    stack=[]
    for each_c in string1:
        if each_c=="(" or each_c=="{" or each_c=="[":
            count=count+1
        else:
            if(len(stack)==0):
                return "NO"
            cur_element=stack.pop()
            if each_c !=cur_element:
                return False            
            count=count-1
        if each_c=="(":
            stack.append(")")
        if each_c=="{":
            stack.append("}")
        if each_c=="[":
            stack.append("]")
        if count<0:
            return False
    if count!=0:
        return False
    else:            
        return True

print braces("([[]])")                            
