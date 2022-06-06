from tkinter import E


def lastfour(number):
    p=number[-1]
    q=number[-2]
    r=number[-3]
    s=number[-4]
    t=int(len(number)-4)
    u="*"*t
    v=str(u)
    print(v+s+r+q+p)

num=input("Enter credit card number:")
lastfour(num)

