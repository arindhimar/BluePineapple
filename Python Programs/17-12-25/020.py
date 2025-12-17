def checkWooland(n):
    if n>0:
        for i in range(1,n+1):
            temp=(i*(2**i))-1
            print(temp)
            if temp==n:
                print("IT is")
                return
            
            
            
        
        print("It is not")
        return 


n=int(input("Enter n"))
checkWooland(n)