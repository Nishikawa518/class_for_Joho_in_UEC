import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def bubblesort(a):
    #arry[0] = arry[1]
    done = False
    while done!=True:
        done = True
        i= 0
        j = len(a)-2
        #print (j)
        while j>i:
            if a[i] > a[i+1]:
                swap(a,i,i+1)
                done = False
                #print (a)
            i+=1
        j-=1

#main
def main():
    args = sys.argv
    arry = [5,1,4,6,0,3,2,7,]
    print (arry)
    bubblesort(arry)
    print (arry)

if __name__ == "__main__":
    main()