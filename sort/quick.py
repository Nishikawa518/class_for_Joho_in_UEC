import random  # randomモジュールをインポート
import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def quicksort(a,start,end):
    #arry[0] = arry[1]
    if end <= start:
        return
    swap(a,end,random.randint(start, end))
    pivot = a[end]
    s=start
    k=start
    while k<end:
        if a[k]<=pivot:
            swap(a,s,k)
            s=s+1
        k=k+1
    swap(a,end,s)
    quicksort(a,start,s-1)
    quicksort(a,s+1,end)
    return

# main関数
def main():
    args = sys.argv
    arry = [5,1,4,6,0,3,2,7,]
    print (arry)
    quicksort(arry,0,len(arry)-1)
    print (arry)

    #print(random.randint(0, 7))  # 0から7の間の乱数を生成して表示

if __name__ == "__main__":
    main()