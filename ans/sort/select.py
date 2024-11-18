import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def selectsort(a):
    #arry[0] = arry[1]
    i=0
    n = len(a)
    while i<n:
        min_index = a[i]
        j=i+1
        while j<n:
            if a[j] < a[min_index]:
                min_index = j
            j=j+1
        swap(a,i,min_index)
        i=i+1

#main
def main():
    args = sys.argv
    arry = [5,1,4,6,0,3,2,7,]
    print (arry)
    selectsort(arry)
    print (arry)

if __name__ == "__main__":
    main()