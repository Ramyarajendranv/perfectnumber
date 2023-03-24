n=int(input("Enter the number:"))
count=0
for i in range(1,n):
    if(n%i==0):
        count=count+i
if(count==n):
    print("Perfect number")
else:
    print("Not a perfect number")
