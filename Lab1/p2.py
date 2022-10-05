# compute gcd of 2 numbers
def gcd(x, y):
    if(y == 0):
        return x
    else:
        return gcd(y, x%y)


print(gcd(8,4), gcd(9,2), gcd(8,0))