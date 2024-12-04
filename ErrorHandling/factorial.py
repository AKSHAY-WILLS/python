def factorial(number):

    factorial=1

    for i in range(1,number+1):

        factorial=factorial*i

    return factorial

print(factorial(4))

def test_factorial():

    assert factorial(4)==True,"not a factorial"

try:

    test_factorial()

    print("test passed")

except Exception as e:

    print("test_failed",e)