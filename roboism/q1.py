def order(list,string):
 if string .lower() =="asc":
     list .sort()
     print(list)
 elif string.lower ()=="desc":
     list .sort(reverse=True )
     print (list)
 elif string.lower()=="none":
     print(list)
 else:
     print("Enter correct information")

list_of_numbers=[]
x=int(input("Enter number of elements in the list:"))
for i in range(x):
    list = int(input("Enter values in list :"))
    list_of_numbers.append(list)

str=input("Enter the string to be sorted in the list:")
     
order(list_of_numbers,str) 
