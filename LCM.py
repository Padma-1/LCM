def LCM(x,y):
    z=x*y
    while x!=0 and y!=0:
        if x>y:
            x%=y
        else:
            y%=x
    return z//(x+y)
a=int(input())
b=int(input())
print(LCM(a,b))
#output:13,9-->117
           
