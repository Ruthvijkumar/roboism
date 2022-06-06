x=int(input("Enter the lower limit :"))
y=int(input("Enter upper limit:"))
if x>y:
    temp = x
    x = y 
    y = temp

for z in range(x,y):
        k=0
        for i in range(2,z//2+1):
         if(z%i==0):
            k=k+1
    
    
        if(k<=0):
            print(z)
            
