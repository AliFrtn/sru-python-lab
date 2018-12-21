a = int(input("Enter a number : "))
b = int(input("Enter another number :"))
if b>a :
    temp=a
    a=b
    b=temp

list1= [0]*100
list2= [0]*100
#################
c=0
i=1
while i<b:
    if b%i==0:
        list1[c]=i
        c+=1
    i+=1
#################
j=0
i=1
while i<a:
    if a%i==0:
        list2[j]=i
        j+=1
    i+=1
#################
k=j-1
while k>0:
    n=c-1
    while n>0:
        if list1[n]==0 or list2[k]==0:
            break
        else:
            if list1[n]==list2[k]:
                print (list1[n])
        
        n-=1
    k-=1

