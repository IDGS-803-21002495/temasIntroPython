#Sentencia de control: if - else

num1 = 3
num2 = 5


if num1 != num2:
    if num1 > num2:
        print("Número {} es mayor que número {}".format(num1,num2))
    else:
        print("Número {1} es mayor que número {0}".format(num1,num2))
else:
    print("")
    