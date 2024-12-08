import sys# main関数
MAX_SIZE = 101

def initstack(s):
    s.append(1)#s[0] is stack top 次に書き込む場所
    for i in range(1,MAX_SIZE):
        s.append('0')

def is_empty(s):
    if s[0]==1:
        return True
    else:
        return False
    

def push(val,s):
    if s[0]==MAX_SIZE:
        print("stack overflow")
        sys.exit(1)
    else:
        s[s[0]]=val
        s[0]+=1
        

def pop(s):
    if s[0]==1:
        print("stack underflow")
        print(s)
        sys.exit(1)
    else:
        s[0]-=1
        return s[s[0]]
        #val = s[s[0]]
        #s[s[0]]='0'
        #return val
        
def check_kokka(val,s):
    popped=pop(s)
    if popped=='(' and val==')':
        #print("1")
        return
    elif popped=='{' and val=='}':
        #print("2")
        return
    elif popped=='[' and val==']':
        #print("3")
        return
    else:
        #print(popped)
        #print(val)
        print("miss")
        sys.exit(1)


def main():
    args = sys.argv
    s=[]
    initstack(s)
    for i in range(1,len(args)):
        if args[i]=='(' or args[i]=='{' or args[i]=='[':
            push(args[i],s)
        else:
            check_kokka(args[i],s)
    #print(pop(s))
    #print(s)
    if is_empty(s)==True:
        print("OK")
    else:
        print("stack is not empty!")


    #print(random.randint(0, 7))  # 0から7の間の乱数を生成して表示

if __name__ == "__main__":
    main()