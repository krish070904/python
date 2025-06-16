'''a = int(input("enter no.1 :"))
b = int(input("enter no.2 :"))
c = int(input("enter no.3 :"))
d = int(input("enter no.4 :"))
max = a
if(b>max):
    max = b 
if(c>max):
    max = c
if(d>max):
    max = d

print(max)'''
a = int(input("enter no.1 :"))
b = int(input("enter no.2 :"))
c = int(input("enter no.3 :"))
d = int(input("enter no.4 :"))
if(a>b and a>c and a>d):
   print(a)
if(b>a and b>c and b>d):
   print(b)
if(c>a and c>b and c>d):
  print(c)
if(d>a and d>b and d>c):
  print(d)