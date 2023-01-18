import sys
n=int(sys.stdin.readline())
mysum=0
xor=0
for i in range(n):
    oper=list(map(int,sys.stdin.readline().split()))
    if oper[0]== 1:
        mysum+=oper[1]
        xor = xor^oper[1]
    elif oper[0]== 2 :
        mysum-=oper[1]
        xor=xor^oper[1]
    elif oper[0] == 3: print((mysum))
    elif oper[0] == 4: print(xor)