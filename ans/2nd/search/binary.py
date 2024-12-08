import random  # randomモジュールをインポート
import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def linear_search(a,val):
    #arry[0] = arry[1]
    for i in range(0,len(a)):
        if a[i]==val:
            return i
    return -1
    
def make_rand_arry(a,length):
    i=0
    while i < length:
        tmp=random.randint(0, 100)
        if linear_search(a,tmp)==-1:
            a.append(tmp)
            i+=1

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

def search(a,val):
    left=0
    right=len(a)-1
    while left<=right:
        m=(left+right)//2
        if val<a[m]:
            right=m-1
        elif val>a[m]:
            left=m+1
        else:
            return m
    return -1

# main関数
def main():
    args = sys.argv
    arry=[]
    length=50
    make_rand_arry(arry,length)
    print (arry)
    quicksort(arry,0,len(arry)-1)
    print(arry)
    print(search(arry,36))
    print(linear_search(arry,36))
    #linear_search(arry,0,len(arry)-1)
    #print (arry)

    #print(random.randint(0, 7))  # 0から7の間の乱数を生成して表示

if __name__ == "__main__":
    main()