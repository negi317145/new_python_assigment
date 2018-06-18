#1.area of circle

def area():
 r=int(input("enter radius of circle"))
 ar=3.14*r*r
 print("area of circle is:",ar)
area()

#2.perfect no

p=[]
def perfect():
  for x in range (1,1000):
      l=[]
      s=0
      for y in range(1,x):
          if x%y==0:
	          l.append(y)
      for a in l:
          s=s+a
      if s==x:
         p.append(x)
perfect()
print(p)
print("\n")	 

#3.multiplication of 12

def multiplication(n,i=1):
    print("12*",i,"=",n*i)
    if i!= 10:
        multiplication(n,i+1)
multiplication(12)


#4.power of a raise to b

def power(a,b):
    if b == 1:
        return a
    else:
        return a * power(a,b-1)
print (power(3,3))

#factorial add into dictionary

n=5
def rec(x):
  if (x==1 or x==0):
    return 1
  else:
    f=x*rec(x-1)
    return f
fact=rec(n)
d = {n:fact}
print(d)
