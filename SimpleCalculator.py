def get_number(num):
    while True:
        operand=input(str(num)+":")
        try:
            return float(operand)
        except:
            print("Invalid operand , Try again!")
x=get_number(1)
y=get_number(2)
sign=input("")
if(sign=="+"):
    print(x+y)
elif(sign=="-"):
    print(x-y)
elif(sign=="*"):
    print(x*y)
elif(sign=="/"):
    if (y!=0):
        print(x/y)
    else:
        print("Invalid operand")
elif(sign=="//"):
    print(x//y)
elif(sign=="%"):
    print(x%y)
elif(sign=="**"):
    print(x**y)
else:
    print("Invalid Sign")

