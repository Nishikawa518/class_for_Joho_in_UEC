import sys# main関数

def main():
    args = sys.argv
    print(len(args))
    print("----------")
    for i in range(1,len(args)):
        if args[i]=='(':
            print("hit")
        else:
            print(args[i])


if __name__ == "__main__":
    main()