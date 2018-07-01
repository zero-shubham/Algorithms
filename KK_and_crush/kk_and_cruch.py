t = int(input())

while(t>0):
    size = int(input('\n'))
    dic = dict()
    tmp = input().split()
    tmp = tmp[:size]
    for i in tmp:
        dic[i] = 1

    size = int(input())
    while(size>0):
        tmp = input()
        if tmp in dic:
            print("\nYes")
        else:
            print("\nNo")
        size-=1
    t-=1
