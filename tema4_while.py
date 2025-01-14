x = 1
num = input("Ingrese un número: ")

while x <= 10:
    res = int(num) * x
    print("{} x {} = {}".format(num,x,res))
    x=x+1