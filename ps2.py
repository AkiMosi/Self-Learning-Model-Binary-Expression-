def genbin(n):
    binset=[]
    for i in range(n**2):
        b=bin(i)[2:]
        b=str(0)*(n-len(b))+b
        binset.append(b)
    return binset
k=int(input("Enter the number of input boolean features 'K' :"))
n=int(input("Enter the number of data points 'N' :"))
data=[]
lis=[]
for i in range (0,n):
    lis=(input().split())
    data.append(lis)
    lis=[]
binset=genbin(2**(k-1))
check=[]
for i in range(len(data)):
    check.append(data[i][len(data[0])-1])
for i in range(nobin):
    
    