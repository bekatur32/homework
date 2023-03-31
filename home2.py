def digit(a):
    b = 0
    for i in a:
        if len(str(i)) % 2 ==0:
            b+=1
            return b
        else:
            return 'rere'

a=[555,901,482,1771]

print(digit(a))