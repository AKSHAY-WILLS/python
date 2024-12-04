


def swap_dec(fn):
    def wrapper(num1,num2):
        if num1<num2:

            (num1,num2)=(num2,num1)
        return fn(num1,num2)
    return wrapper


def round_dec(fn):
    def wrappper(num1,num2):
        num1=round(num1)
        num2=round(num2)
        return fn(num1,num2)
    return wrappper

@round_dec
@swap_dec
def add_number(num1,num2):

    return num1+num2

@round
@swap_dec
def subtraction(num1,num2):
    

    return num1-num2

@round_dec
@swap_dec
def division(num1,num2):

    return num1/num2

print(subtraction(2.2,9))
print(division(2.3,10))
print(add_number(0.5,0.7))