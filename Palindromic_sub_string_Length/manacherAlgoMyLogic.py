def prime(num):
    if num > 1: 
        # Iterate from 2 to n / 2 
        for i in range(2, num//2): 
            if (num % i) == 0: 
                print("NOT PRIME") 
                break
        else: 
            print("PRIME") 
    else: 
        print("NOT PRIME")

def main():
    terms = int(input())
    while(terms!=0):
        s = input()
        s = list(map(str,s))
        s = '#'.join(s)
        s = '^#'+s+'#$'
        #print(s)
        n= len(s)
        #print(n)
        arr = [0] * n

        i = 0

        while(i<n):
            flag=0
            #print(arr)

            if arr[i] <= 1:
                palL = 1
                j = 1
            else:
                palL = arr[i]
                j = (arr[i] // 2) + 1


            while((i - j) >= 0 and (j + i) < n  ):
                if s[i - j] == s[j+i]:
                    palL += 2
                else:
                    break
                j += 1
            

            arr[i] = palL
            #print("arr[i]=",arr[i],"palL=",palL)
            if(i + (palL//2) == n-1):
                break


            #finding the next position for i
            if palL>3:
                x = 1

                while(i+x<n and i-x>=0):
                    arr[i + x] = arr[i - x]
                    
                    if (i+x) + (arr[i+x] // 2) == (arr[i]//2) + i:
                        flag=1
                        i += x
                        break
                    elif (i+x) + (arr[i+x] // 2) > (arr[i]//2) + i:
                        arr[i+x] = arr[i+x] -  ( ( (arr[i+x]//2) + (i+x) ) -  (i+(arr[i]//2)) )*2
                        i += x
                        flag=1
                        break
                    x += 1


            if flag==0:
                i += 1

        prime(max(arr)//2)
        terms -= 1

if __name__ == "__main__":
    main()