def operation(x,y,z):
    
    x=float(x)
    z=float(z)
    if y=='+':
      print(x+z)
    elif y=='-':
      print(x-z)
    elif y=='*':
      print(x*z)
    elif y=='/':
      print(x/z)
    else:
      print("error!")


x=input ("Enter the first number:")
y=input ("Enter the operator:")
z=input ("Enter the third number:")
operation(x,y,z)            
    