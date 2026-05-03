a=(1,2,"Hello")
print(a)
b=(-1,-1,1,2,3)
print(b)
d=(9)
c=(-1,-1,1,2,3)+(9,)
print(c)
count=0
for i in c:
    if i==-1:
        count+=1
print("number of occurunces of -1 =", count)
print(c[2:5])

