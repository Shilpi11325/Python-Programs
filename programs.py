#Hello World
print ("Hello World!")

#Arithmetic Operations 
a= int(input ("enter first number:"))
b= int(input ("enter second number:"))
print ("sum=",a+b)
print ("sub=",a-b)
print ("mul=",a*b)
print ("div=",a/b)
print ("avg=",(a+b)/2)

#Conditional Statements 
a= int (input ("enter first number"))
b= int (input ("enter second number"))
c= int (input ("enter third number"))
if (a>=b):
    print ("first is largest number")
elif (b>=c):
    print ("second is largest number")
else:
    print ("third is largest number")

#For Loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#Break Statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  
    print(num)

#Continue Statement 
for i in range(1, 6):
    if i == 3:
        continue  
    print(i)

#While Loop
i = 1
while i <= 5:
    print(i)
    i += 1  

#List with methods
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.insert(1, "orange")
fruits.extend(["grapes", "kiwi"])
fruits.remove("banana")
fruits.pop(2)
fruits.sort()
fruits.reverse()
print(fruits)

#Tuple with methods
my_tuple = (10, 20, 30, 20, 40)

print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))

new_tuple = my_tuple + (50, 60)
print("New Tuple:", new_tuple)

print("Length:", len(new_tuple))
print("Is 40 in tuple?", 40 in new_tuple)

#Dictionary with methods 
dict = {"name": "Shilpi", "age": 21, "city": "Bhopal"}

print(dict["name"])          
print(dict.get("age"))       

dict["age"] = 21
dict["country"] = "India"

print(dict.keys())          
print(dict.values())         
print(dict.items())         

dict.pop("city")
dict.popitem()

new_dict = dict.copy()

print("Original:", dict)
print("Copy:", new_dict)

#Set with methods
A = {1, 2, 3}
B = {3, 4, 5}

A.add(6)
A.update([7, 8])

A.remove(2)
A.discard(10)

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))
print("Is B subset of A?", B.issubset(A))

#Odd or Even Numbers 
num= int (input ("enter a number"))
if (num % 2==0):
    print ("number is even")
else:
    print ("number is odd")

#Prime Number
n= int (input ("enter a number"))
if n>1:
    for i in range (2,n):
        if n%2==0:
            print ("not prime")
            break
        else:
            print ("prime")

#Reverse a number
n= int (input ("enter a number"))
rev=0
while n>0:
    rev=rev*10+n%10
    num//=10
    print ("reversed:",rev)

#Palindrome Number
num=int (input ("enter a number"))
if (num == num [::-1]):
    print ("palindrome")
else:
    print ("not palindrome")

#Armstrong Number
num= int (input ("enter a number"))
sum= sum (int (d)**3 for d in str(num))
if (sum == num):
    print ("armstrong")
else:
    print ("not armstrong")


#Multiplication Table 
n= int (input ("enter a number"))
for i in range (1,11):
 print (f"{n}x{i}={n*i}")

#Calender
import calender
year = int (input ("enter year:"))
month = int (input ("enter month:"))
print (calender.month (year,month))

#Leap Year
year= int (input ("enter a number"))
if (year%400==0)or (year%100!=0 and year%4==0):
    print ("leap year")
else:
    print ("not a leap year")

#Factorial
n= int (input ("enter a number"))
fact = 1
for i in range (1,n+1):
    fact*=i
    print ("factorial=",fact)

#Factor
n= int (input ("enter a number"))
print ("factors are:")
for i in range (1,n+1):
    if n%i == 0:
        print (i)

#Fabonacci Series
n= int (input ("enter a number"))
a,b=0,1
for i in range (n):
    print (a,end=" ")
    a,-b=b,a+b

#Simple Interest 
p= float (input ("enter principle:"))
r= float (input ("enter rate:"))
t= float (input ("enter time:"))
print (p*r*t)/100

#Star Pattern 
n= int (input ("enter number of rows:"))
for i in range (1,n+1):
    print ("*"*i)

#Built-in Functions 
a = 10
print("Type of a:", type(a))

name = "Shilpi"
print("Length of name:", len(name))

numbers = [5, 12, 3, 9, 1]
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Sum of numbers:", sum(numbers))
print("Sorted list:", sorted(numbers))

user_name = input("Enter your name: ")
print("Hello,", user_name)

#User define Function
def add(a, b):
    result = a + b
    print("Sum =", result)

add(10, 20)

#Class and Object 
class student:
    name ="Shilpi"
s1=student()
print (s1.name)

s2=student()
print (s2.name)

#OOPS
#Encapsulation
class Student:
    def __init__(self):
        self.name = "Shilpi"       
        self.__marks = 90         

    def show(self):
        print(self.name)
        print(self.__marks)

s = Student()
s.show()

#Getter and Setter
class Student:
    def __init__(self):
        self.__marks = 0

    def setMarks(self, marks):
        if marks >= 0:
            self.__marks = marks

    def getMarks(self):
        return self.__marks

s = Student()
s.setMarks(95)
print(s.getMarks())


#Inheritence 
#Single Inheritence 
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

#Multilevel Inheritence
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()

#Multiple Inheritence 
class Father:
    def quality1(self):
        print("Father quality")

class Mother:
    def quality2(self):
        print("Mother quality")

class Child(Father, Mother):
    pass

c = Child()
c.quality1()
c.quality2()

#Hierarchical Inheritence
class Parent:
    def display(self):
        print("Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.display()
obj2.display()


#Polymorphism 
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

#Abstraction
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

class BMW(Car):
    def start(self):
        print("BMW Started")

b = BMW()
b.start()







