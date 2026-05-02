# class BankAccount:
  
#   def __init__(self,acc_no,owner_name,balance):
#     self.acc_no=acc_no
#     self.owner_name=owner_name
#     self.__balance=balance
    
#   def deposit(self,amount):
#       self.__balance+=amount
#       print(f"Deposited {amount}. New balance: {self.__balance}")
      
#   def withdraw(self,amount):
#       if amount > self.__balance:
#           print("Insufficient funds")
#       else:
#           self.__balance-=amount
#           print(f"Withdrew {amount}. New balance: {self.__balance}")
#   def get_balance(self):
#     print(f"Current balance: {self.__balance}")        
         
# b1=BankAccount("123456","Shradha",1000)         
# b1.deposit(500)
# b1.withdraw(200)
# b1.get_balance()
         
         
         
# class Book:
  
#   def __init__(self,title,author,list_of_review):
#     self.title=title
#     self.author=author
#     self.list_of_review=list_of_review
    
#   def add_review(self,review):
#     self.review=review
#     self.list_of_review.append(self.review)
    
#   def count_reviews(self):
#     print(len(self.list_of_review))
  
#   def show_review(self):
#     for review in self.list_of_review:
#       print(review)
    
# b1=Book("sinhagad","sambhaji maharaj",["good","excellent"])
# b1.add_review("exhausted") 
# b1.count_reviews()
# b1.show_review()   
    
             
# class Student:
  
#   def __init__(self,name,roll_no,marks):
#     self.__name=name
#     self.__roll_no=roll_no
#     self.__marks=marks
    
#   def get_info(self):
#     print(self.__name,self.__marks,self.__roll_no)  
    
#   def set_info(self,new_name,new_marks,new_roll_no):
#     if new_marks <0 : print("invalid marks")
#     else: self.__marks=new_marks
#     if new_roll_no >= 1 and new_roll_no <= 100:
#       self.__roll_no=new_roll_no
#     else: print("invalid roll_no")  
#     if len(new_name) == 0: print("invalid name")
#     else:  
#       self.__name=new_name
    
# s1=Student("sara",88,200)
# s1.get_info()    
# s1.set_info("saru",300,100)  
# s1.get_info()                 
                 
                 
# class shape:
#    def area(self):
#        pass
# class circle(shape):
#    PI=3.14
#    def __init__(self,redius):
#      self.redius=redius
#    def area(self):
#      print(2*circle.PI*self.redius)  
# class rectangle(shape):
#     def __init__(self,length,bredth):
#       self.length=length
#       self.bredth=bredth
#     def area(self):
#          print(self.length*self.bredth)
# c1=circle(5)  
# c1.area()         

# r1=rectangle(12,12)
# r1.area()
      
       
# class Vehicle:  
#    def __init__(self,brand,model):
#        self.brand=brand
#        self.model=model
       
#    def show_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)   
# class car(Vehicle) :
#   def __init__(self,seats,brand,model):
#     super().__init__(brand,model)
#     self.seats=seats
  
#   def show_details(self):
#         super().show_details()
#         print("Seats:", self.seats)
        
# class Bike(Vehicle):
#    def __init__(self,engine,brand,model):
#     super().__init__(brand,model)
#     self.engine=engine
    
#    def show_details(self):
#         super().show_details()
#         print("Engine CC:", self.engine)


# # Driver Code
# car1 = car("Toyota", "Fortuner", 7)
# bike1 = Bike("KTM", "Duke", 200)

# print("Car Details:")
# car1.show_details()

# print("\nBike Details:")
# bike1.show_details() 
      
  
                            
# class Employee:
#   def calc_sal(self):
#     pass          
  
# class Intern:
#   def __init__(self,hours,hour_sal):
#     self.hours=hours
#     self.hour_sal=hour_sal
#   def calc_sal(self):
#     print(self.hours*self.hour_sal) 
    
# class Fulltimeemployee(Employee):
#    def __init__(self,hours,hour_sal):
#     self.hours=hours
#     self.hour_sal=hour_sal
#    def calc_sal(self):
#     print(self.hours*self.hour_sal) 
                           
# class contractEmployee(Employee):
#    def __init__(self,hours,hour_sal):
#     self.hours=hours
#     self.hour_sal=hour_sal
#    def calc_sal(self):
#     print(self.hours*self.hour_sal) 
    
# c1=contractEmployee(40,300) 
# c1.calc_sal()   
                             
                             
# from abc import ABC, abstractmethod

# # Abstract Class
# class Employee(ABC):

#     @abstractmethod
#     def calculate_salary(self):
#         pass


# # Subclass 1: Intern
# class Intern(Employee):
#     def __init__(self, stipend):
#         self.stipend = stipend

#     def calculate_salary(self):
#         print("Intern Salary:", self.stipend)


# # Subclass 2: Full Time Employee
# class FullTimeEmployee(Employee):
#     def __init__(self, salary, bonus):
#         self.salary = salary
#         self.bonus = bonus

#     def calculate_salary(self):
#         total = self.salary + self.bonus
#         print("Full Time Salary:", total)


# # Subclass 3: Contract Employee
# class ContractEmployee(Employee):
#     def __init__(self, hourly_rate, hours):
#         self.hourly_rate = hourly_rate
#         self.hours = hours

#     def calculate_salary(self):
#         total = self.hourly_rate * self.hours
#         print("Contract Salary:", total)


# # Driver Code
# e1 = Intern(10000)
# e2 = FullTimeEmployee(50000, 10000)
# e3 = ContractEmployee(500, 40)

# e1.calculate_salary()
# e2.calculate_salary()
# e3.calculate_salary()        



# class person:
#     def __init__(self,name,age=None,address=None):
#         self.name=name
#         self.age=age
#         self.address=address
#     def get_info(self): 
#         print("name is",self.name)
#         print("age is",self.age)
#         print("address is",self.address)   
       

                
# p1=person("sara")             
# p1.get_info()          
# from abc import ABC, abstractmethod
# class player:
#     player_count=0
#     def __init__(self,name,level):
#         self.name=name
#         self.level=level
#         player.player_count+=1
#     @classmethod    
#     def display(cls):
#         print(f"player count is {cls.player_count}")    
        
# p1=player("sara","hard")
# p2=player("samu","easy")
# player.display()      


# class Herbivore:
#     def eat_plants(self):
#         print("Eats plants 🌿")

# class Carnivore:
#     def eat_meat(self):
#         print("Eats meat 🍖")

# class Omnivore:
#     def eat_both(self):
#         print("Eats both plants and meat 🍽️")


# class Bear(Herbivore, Carnivore, Omnivore):
#     def info(self):
#         print("Bear is an omnivorous animal")


# b = Bear()

# b.info()
# b.eat_plants()
# b.eat_meat()
# b.eat_both()





