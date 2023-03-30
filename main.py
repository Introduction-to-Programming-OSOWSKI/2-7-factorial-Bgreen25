def factorial(x):
    numA = 1
    for i in range(1,x+1):
        numA = numA*i
        
    return numA

print (factorial(5))