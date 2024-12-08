import random  # randomモジュールをインポート
import sys

def linear_search(a,val):
    #arry[0] = arry[1]
    for i in range(0,len(a)):
        if a[i]==val:
            return i
    return -1
    


# main関数
def main():
    args = sys.argv
    arry=[]
    i=0
    while i < 10:
        tmp=random.randint(0, 50)
        if linear_search(arry,tmp)==-1:
            arry.append(tmp)
            i+=1
    print (arry)
    #linear_search(arry,0,len(arry)-1)
    #print (arry)

    #print(random.randint(0, 7))  # 0から7の間の乱数を生成して表示

if __name__ == "__main__":
    main()