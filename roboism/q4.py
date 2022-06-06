def string_doubled(str):
   a=[]
   b=""
   for i in range(len(str)):
       a.append(str[i]*2)

   for j in range(len(a)):
            b=b+a[j]
   print(b)

string = input("Enter a string:")
string_doubled(string)