list=[]
num=int(input("enter length of list"))
print("enter list")
for i in range(num):
 data=int(input())
 list.append(data)
 print(list)
 num1=int(input("enter element "))
 if num1 in list:
  print(num1)
 else:
  print(list)