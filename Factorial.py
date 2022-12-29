#https://www.freecodecamp.org/news/intro-to-algorithms-with-python/


def interactive_factorial(n):
    fact =1
    for i in range(2,n+1):
        fact *=i
    return fact




def recur_factorial(n):
    temp=0
    if n==1:
        return n
    else:
        temp=recur_factorial(n-1)
        temp =temp *n
    return temp


#print(interactive_factorial(5))
print(recur_factorial(5))