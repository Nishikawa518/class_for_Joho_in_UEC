import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def bubblesort(a):


#main
def main():
    args = sys.argv
    arry = [5,1,4,6,0,3,2,7,]
    print (arry)
    bubblesort(arry)
    print (arry)

if __name__ == "__main__":
    main()