# python
# You're analyzing weather data. Given a list of temperatures, filter out all temperatures below 15°C and create a new list using list comprehension. Input: [5, 20, 12, 25, 8, 30, 3, 18]
l=[5, 20, 12, 25, 8, 30, 3, 18]
filtered_temp=[temp for temp in l if temp<=15]
print(filtered_temp)

# An e-commerce platform filters product names by length. Given a list of product names, create a list containing only names with more than 5 characters using list comprehension. Input: ['phone', 'keyboard', 'mouse', 'monitor', 'usb']
products=['phone', 'keyboard', 'mouse', 'monitor', 'usb']
filteres_prod=[prod for prod in products if len(prod)>5]
print(filteres_prod)

# A restaurant wants to calculate ingredient costs. Given quantities (in kg), calculate total cost where each kg costs as its square value. Use list comprehension. Input: [2, 3, 5, 1, 4]
resturant =[2, 3, 5, 1, 4]
filtered_res=[res**2 for res in resturant ]
print(sum(filtered_res))

# A password validator extracts uppercase letters to check password strength. Given a string, extract all uppercase letters using list comprehension. Input: 'HeLLo_World_123'
inp='HeLLo_World_123'
upper_pass=[i for i in inp if i==i.upper()]
print(upper_pass)

# HR system filters eligible candidates for senior roles (age 30+). Given (name, age) tuples, extract names of eligible people using list comprehension. Input: [('Alice', 28), ('Bob', 32), ('Charlie', 25), ('Diana', 35)]
candidate=[('Alice', 28), ('Bob', 32), ('Charlie', 25), ('Diana', 35)]
filtered_cand=[i for i in candidate if i[1]>30]
print(filtered_cand)

# Store inventory manager organizes items by storage racks. Print all item IDs from 1 to 100 where ID is divisible by 7 using a loop.
for i in range(1,100):
    if i%7==0:
        print(i)

# Calculate monthly revenue. Given a list of daily sales, calculate total revenue for the month using a loop. Input: [1200, 1500, 980, 2100, 1300, 1800, 900]
revenue=[1200, 1500, 980, 2100, 1300, 1800, 900]
sums=0
for i in revenue:
    sums+=i
print(sums)
     
# Log analyzer reads system errors in reverse chronological order. Given a list of log messages, print each from last to first. Input: ['Login error', 'DB timeout', 'File not found', 'Connection refused']
error=['Login error', 'DB timeout', 'File not found', 'Connection refused']
print(error[::-1])

     
# Banking app filters successful transactions. Given transaction amounts (positive=credit, negative=debit), print only successful deposits using a loop. Input: [500, -200, 1500, -50, 2000, -100, 300]
trans=[500, -200, 1500, -50, 2000, -100, 300]
for i in trans:
    if i>0:
        print(i)

     
# Website analytics finds peak traffic hour. Given hourly traffic numbers, find the hour with max traffic using a loop (no max() function). Input: [150, 320, 280, 450, 210, 380, 290, 500, 180]
traffic=[150, 320, 280, 450, 210, 380, 290, 500, 180]
maxs=0
for i in traffic:
    if i>maxs:
        maxs=i
print(maxs)

     
# Classes Practice Questions
# School management system tracks student records. Create a Student class with name, student_id, and grade. Initialize and display a student's details.
class student():
    def __init__(self,name,student_id,grade):
        self.name=name
        self.student_id=student_id
        self.grade=grade
    def prints(self):
        print(f"student_name: {self.name} and student id: {self.student_id} and grade: {self.grade}")

a=student('harsh',5,'A')
a.prints()

     
# Construction company calculates land plots. Create a Rectangle class with length and width. Add methods for area() and perimeter(). Test with 5x10 plot.
class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)
    def perimeter(self):
        print(2(self.length+self.width))
R=Rectangle(5,10)
R.area()
R.perimeter()

     
# Bank creates account management system. Build BankAccount class with holder name and balance. Implement deposit() and withdraw(). Perform: deposit 1000, withdraw 200, deposit 500.
class BankAccount():
    def __init__(self,holdername,balance):
        self.holdername=holdername
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
account=BankAccount('harsh',0)
account.deposit(1000)
account.withdraw(200)
account.deposit(500)
print(account.balance)
     
# Car dealership manages inventory. Create Car class with make, model, year, price. Add display_info() method. Create 2 cars and show details.
class car():
    def __init__(self,make, model, year, price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price
    def display_info(self):
        print(f"{self.make}, {self.year} , {self.model} and {self.price}")
car1=car('hp','honda1',2025,5000000)
car1.display_info()
car2=car('kia','125',2026,5000890)
car2.display_info()
     
# Public library digital catalog system. Create Book class with title, author, isbn, publication_year. Add display_info() method. Add 'To Kill a Mockingbird' by Harper Lee.
class Book():
    def __init__(self,title, author, isbn, publication_year):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.publication_year=publication_year
    def display_info(self):
        print(f" Add {self.title} by {self.author}")
B1=Book('To Kill a Mockingbird','Harper Lee','op',2026)
B1.display_info()
     
# Dictionaries Practice Questions
# University processes exam results. Given student scores dict, print names scoring 85+. Input: {'Alice': 92, 'Bob': 78, 'Charlie': 88, 'Diana': 81, 'Eve': 95}
dict={'Alice': 92, 'Bob': 78, 'Charlie': 88, 'Diana': 81, 'Eve': 95}
for k,v in dict.items():
    if v>85:
        print(k)

     
# E-store extracts product catalog. Given product_name: category dict, print all product names. Input: {'laptop': 'electronics', 'shirt': 'clothing', 'book': 'media', 'chair': 'furniture'}
prod={'laptop': 'electronics', 'shirt': 'clothing', 'book': 'media', 'chair': 'furniture'}
print(prod.keys())

     
# Grocery store generates stock report. Given item_name: quantity dict, print all stock quantities. Input: {'apples': 45, 'oranges': 30, 'bananas': 60, 'grapes': 25}
grocery={'apples': 45, 'oranges': 30, 'bananas': 60, 'grapes': 25}
print(grocery.values())

     
# Electronics store finds premium item. Given product: price dict, find the most expensive item. Input: {'laptop': 1200, 'mouse': 45, 'keyboard': 120, 'monitor': 350, 'headphones': 95}
electronic={'laptop': 1200, 'mouse': 45, 'keyboard': 120, 'monitor': 350, 'headphones': 95}
max_prod=''
max_price=0
for k,v in electronic:
    if v>max_price:
        max_price=v
        max_prod=k
print(max_prod)
     
# HR consolidates employee databases. Merge two employee ID: name dicts. dict1: {101: 'Alice', 102: 'Bob'}, dict2: {103: 'Charlie', 104: 'Diana'}. Output merged dict.
dict1={101: 'Alice', 102: 'Bob'}
dict2= {103: 'Charlie', 104: 'Diana'}

