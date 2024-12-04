num1=int(input("enter first number"))

num2=int(input("enter second number"))

try:
    result=num1/num2

    print(result)

except:
    num2=int(input("enter second number"))
    result=num1/num2

    print(result)

finally:
    print("file operatiion")

    print("database commit")