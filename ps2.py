def genbin(n):
    binset=[]
    for i in range(n**2):
        b=bin(i)[2:]
        b=str(0)*(n-len(b))+b
        binset.append(b)
    return binset

def tobin(n):      # this is to generate binary codes for n dimenshiiooon 8)
   out=[]
   for i in range(pow(2,n)):
       b = bin(i)[2:]
       b = str(0) * (n - len(b)) + b
       out.append(b)
   return out

def boolean(code,K):    #give code and dimension(K) 8) to return boolean expression
   a=[]
   x=tobin(K)
   for i in range(K):
       a.append(chr(65+i))
   n = pow(2,K)
   #t=""
   temp=""
   for i in range(n):
       if(code[i]=='1'):
           if(temp!=""):
               temp+="+"
           for j in range(K):
               temp+=a[j]
               if(x[i][j]=='0'):
                   temp+='`'
   if(temp==""):
       temp='0'
   return temp
#k=int(input("Enter the number of input boolean features 'K' :"))
#n=int(input("Enter the number of data points 'N' :"))
#data=[]
#lis=[]
#for i in range (0,n):
#    lis=(input().split())
#    data.append(lis)
#    lis=[]
data=[['0', '0', '0'], ['0', '1', '0'], ['1', '0', '0']]
k=len(data[0])
n=len(data)
binset=genbin(2**(k-1))
check=[]
j=0
for i in range(len(data)):
    check.append(data[i][len(data[0])-1])
for i in range(len(check)):
    j=0
    while(j<len(binset)):
        if(check[(len(check)-1)-i]!=binset[j][(len(check)-1)-i]):
            print(i,check[(len(check)-1)-i],binset[j][(len(check)-1)-i],binset[j])
            binset.pop(j)
        j=j+1
        
