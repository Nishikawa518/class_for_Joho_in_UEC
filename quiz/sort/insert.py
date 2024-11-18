import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def insertsort(a):
    #arry[0] = arry[1]
    i=1
    n = len(a)
    while i<n:
        j= #jの開始番号を入れる
        while j>=0:
            if a[]<a[]:#入れ替える条件
                break
            swap(a,,)#入れ替える番地
            j=j-1
        i=i+1

#main
def main():
    args = sys.argv
    arry = [5,1,4,6,0,3,2,7,]
    print (arry)
    insertsort(arry)
    print (arry)

if __name__ == "__main__":
    main()