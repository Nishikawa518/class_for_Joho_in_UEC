import sys
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#main
def main():
    args = sys.argv
    print(fib(8))

if __name__ == "__main__":
    main()