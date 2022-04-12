a=int(input())
b=int(input())
d=[]
while b>=1:
    c=b%a
    b=b//a
    if a==16:
        d.append("{0:x}".format(c).upper())
    else:
        d.append(str(c))
d.reverse()
print("".join(d))
