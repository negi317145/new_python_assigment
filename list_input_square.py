list=[]
num=int(input("enter length of list"))
print("enter list")
for i in range(num):
 data=int(input())
 list.append(data)
print(list)
list1=[]
for i in range(num):
 list1=[list[i]**2]
 print(list1) 