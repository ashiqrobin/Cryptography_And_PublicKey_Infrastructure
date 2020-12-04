def xgcd(a, b):
    """
    gcd(e,φ(n))=1
    ed≡1(modφ(n))
    EED calculates x and y such that ax+by=gcd(a,b). Now let a=e, b=φ(n), and thus gcd(e,φ(n))=1 by definition
    ex+φ(n)y=1
    ex≡1(modφ(n))
    x=d 
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return int(a), int(old_x), int(old_y)
if __name__ == "__main__":
    
    a = int(input("Value1:"))
    b = int(input("Value2:"))
    gcd,x,y = xgcd(a, b)
    print("a*x+b*y=gcd(a,b):",a,"*","(",x,")","+",b,"*","(",y,")","=",gcd)
    if gcd ==1:
        d=b+x
        print("The Key Exponent is",d)
    else:
        print("No Key Exponent")

#print (gcd)
#print (x)
#print (y)


