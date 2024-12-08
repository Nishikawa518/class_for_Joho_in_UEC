import sys
def gcd(x,y):
    if x==y:
        return x
    elif x>y:
        return gcd(x-y,y)
    else:
        return gcd(x,y-x)

#main
def main():
    args = sys.argv
    arry = [60,18]
    print (arry)
    print (gcd(arry[0],arry[1]))

if __name__ == "__main__":
    main()