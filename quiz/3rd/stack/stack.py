import sys# main関数
MAX_SIZE = 101

def initstack(s):
    s.append(1)#s[0] is stack top 次に書き込む場所
    for i in range(1,MAX_SIZE):
        s.append('0')

def push(val,s):
    if :#条件式を加える
        print("stack overflow")
        sys.exit(1)
    else:
        s[s[0]]=val
        s[0]+=1
        

def pop(s):
    if :#条件式を加える
        print("stack underflow")
        print(s)
        sys.exit(1)
    else:
        s[0]-=1
        return s[s[0]]
        #val = s[s[0]]
        #s[s[0]]='0'
        #return val
        



def main():
    args = sys.argv
    s=[]
    initstack(s)
    push('a',s)
    push('b',s)
    print(pop(s))
    push('c',s)
    print(pop(s))
    print(pop(s))
    #print(pop(s))
    print(s)


    #print(random.randint(0, 7))  # 0から7の間の乱数を生成して表示

if __name__ == "__main__":
    main()