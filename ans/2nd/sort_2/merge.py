import random  # randomモジュールをインポート
import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def merge(a1,i1,end1,a2,i2,end2):
    b=[]
    while i1<=end1 or i2 <=end2:
        if i1 > end1:
            b.append(a2[i2])
            i2+=1
        elif i2>end2:
            b.append(a1[i1])
            i1+=1
        elif a1[i1] > a2[i2]:
            b.append(a2[i2])
            i2+=1
        else:
            b.append(a1[i1])
            i1+=1
    return b

def mergesort(a,start,end):
    #arry[0] = arry[1]
    if end <= start:
        return
    k=(start+end)//2
    mergesort(a,start,k)
    mergesort(a,k+1,end)
    b=merge(a,start,k,a,k+1,end)
    for i in range(0,len(b)):
        a[start+i] = b[i]
    return

# main関数
def main():
    args = sys.argv
    arry = [5,1,4,6,0,3,2,7]
    print (arry)
    mergesort(arry,0,len(arry)-1)
    print (arry)

    #print(random.randint(0, 7))  # 0から7の間の乱数を生成して表示

if __name__ == "__main__":
    main()