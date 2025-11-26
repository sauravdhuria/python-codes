def fact(n):
    if n<0:
        return print("Factorial of negative number is not defined")
    elif n==0 or n==1:
        return 1
    else:
        factorial = n*fact(n-1)
        return factorial


print(fact(10))
