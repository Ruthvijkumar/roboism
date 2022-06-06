x=input("Enter the no.of elements in the list:" )
y=[]
for i in range(int(x)):
    a=input(":")
    y.append(x)
max = 0
r = []
for j in range(len(y)-1):
    count = 1
    for k in range(j+1,len(y)):
        if j!=k and y[j]==y[k]:
            count += 1
            if max<=count:
                r.append(str(y[j]))

print(r)
for l in range(len(r)):
    print(str(r[l])+"is the element in list having maximum frequency and frequency is"+str(max))     