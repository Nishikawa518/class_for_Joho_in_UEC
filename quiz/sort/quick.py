import random  # randomモジュールをインポート
import sys

def swap(arry,a,b):
    tmp = arry[a]
    arry[a] = arry[b]
    arry[b] = tmp

def quicksort(a,start,end):
    #arry[0] = arry[1]
    if : #要素数が1つ以下であるとき何も行わずに終了
        return
    swap(a,end,random.randint(start, end)) #pivotを設定
    pivot = a[end]
    s=start
    k=start
    while k<end:
        #a[pivot]以下と以上に2分割し、以上の一番左の要素のインデックスをsとする
    swap(a,end,s)
    #pivot以下の要素についてquicksort
    #pivotより大きいの要素についてquicksort
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