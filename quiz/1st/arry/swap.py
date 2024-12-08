import sys

def swap(arry,a,b):
    #配列arryのa番目とb番目の内容を入れ替える

#main
def main():
    args = sys.argv
    arry = [5,1,4,6,0,3,2,7,]
    print (arry)
    swap(arry,0,3)

    print (arry)

if __name__ == "__main__":
    main()