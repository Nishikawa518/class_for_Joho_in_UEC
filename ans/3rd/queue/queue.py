import sys# main関数
MAX_SIZE = 103

def initqueue(q):
    q.append(2)#q[0] is queue rear 次に書き込む場所
    q.append(2)#q[1] is queue front 次に読む場所
    for i in range(2,MAX_SIZE):
        q.append('0')

def add_queue_index(index):
    if index<MAX_SIZE-1:
        return index+1
    else:
        return 2

def enqueue(val,q):
    q[q[0]]=val
    q[0]=add_queue_index(q[0])
    if q[0]==q[1]:
        print("queue overflow")
        sys.exit(1)
        

def dequeue(q):
    if q[0]==q[1]:
        print("queue underflow")
        print(q)
        sys.exit(1)
    else:
        val=q[q[1]]
        q[1]=add_queue_index(q[1])
        return val




def main():
    args = sys.argv
    q=[]
    initqueue(q)
    enqueue('a',q)
    enqueue('b',q)
    print(dequeue(q))
    enqueue('c',q)
    print(dequeue(q))
    print(dequeue(q))
    #print(dequeue(q))
    print(q)


    #print(random.randint(0, 7))  # 0から7の間の乱数を生成して表示

if __name__ == "__main__":
    main()