#create a circle class init with radius

class circle:
	radius=9
	def get_area(self):
		print("area is:",3.14*self.radius*self.radius)
	def get_circum(self):
		print("circumferemce is:",2*3.14*self.radius)
obj=circle()
obj.get_area()
obj.get_circum()


#class student and init with name and roll no

class student:
  name="himanshu"
  roll_no=6316029
  def display(self):
    print("name:",self.name)
    print("roll_no:",self.roll_no)
obj=student()
obj.display()


#create a class temperature with two methods

class temp:
  def temp_degree(self):
    c=int(input("enter temp in celcius"))
    c1=1.8*c+32
    print("temp in degree is:",c1)
  def temp_farenheit(self):
    f=int(input("enter temp in farenheit"))
    f1=(f-32)/1.8
    print("temp in farenheit is:",f1)
obj=temp()
obj.temp_degree()
obj.temp_farenheit()


#movie details init with name,artist,release

class movie:
  name="avenger"
  artist="tony stark"
  releasing_date="20-04-2018"
  def display(self):
    print("detail:\n","\n",self.name,"\n",self.artist,"\n",self.releasing_date,"\n")
  def update(self):
    name="pk"
    artist="ameer khan"
    releasing_date="22-12-2015"
    print("update details:\n","\n",name,"\n",artist,"\n",releasing_date)
	
obj=movie()
obj.display()
obj.update()

#expenditures and savings

class expenditures:
    expenditures=60000
    savings=10000
    def display(self):
        print("expenditures and savings:",self.expenditures,self.savings)
    def total(self):
        totall=self.expenditures+self.savings
        return totall
    def salary(self,a):
        self.totall=a
        print("total salary:",self.totall)
obj=expenditures()
obj.display()
obj.display()
a=obj.total()
obj.salary(a)