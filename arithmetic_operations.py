def arithetic_operation(opr,*args):
    result=0
    if opr=="add":
        for i in args:
            result+=i
        return result
    elif opr=="sub":
        maximum=max(args)
        result=maximum
        for i in args:
            if i==maximum:
                pass
            else:
                result-=i
        return result
    elif opr=="mul":
        result=1
        for i in args:
            result*=i
        return result
    elif opr=="div":
        return args[0]/args[1]
        
        
print(arithetic_operation("add",5,10))
print(arithetic_operation("sub",5,10))
print(arithetic_operation("mul",5,10))
print(arithetic_operation("div",5,10))