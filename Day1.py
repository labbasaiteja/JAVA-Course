age = input("enter age") #user input
print("My age is",age)

l , b = input("enter length and breadth").split() #taking multiple inputs
print("entered l and b are", l, b)

age_input = input("enter age: ")#taking string input as default it will be string
age = int(age_input)#converting string to int

if age < 0:
    print("Please enter valid age")
elif age < 18:
    print("minor")
elif age >=18 and age < 65:
    print("adult")
else:
    print("senior citizen")            


age = int(input("enter age "))#converting string to int while giving value
print(age)

price = float(input("enter the price of rose"))#typecasting
print(price)