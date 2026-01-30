print("Hello Python!")
print("I am chavda sejal")
a = 35
b = 'bob'
print(a,b)
c = 1
print(a + c)
print(type(a))
print("The value of A :",end=' ')
print((a)) 
print('Hello {} you are {} years old !!'.format(b,a))
one = float(input('Enter your marks : '))
two = input('Enter Your Name : ')
print(f'Welcome{two},you get{one:.2f} marks')
li = [1,2,3,4,5,6,7,8,9,'a','b']
li.append(10)
li.extend([11,12,13])
li.remove('a')
li.pop()
li.insert(2, 25)
print(li.pop())
print(li[4:7])
print(li)
print(li.index(10))
print(li.count(10))

mytuple = ("apple", "banana", "cherry", "apple")
Employee = {"Name": "Johnny", "Age": 32, "salary":26000,"Company":"^TCS"} 

print(mytuple.count("apple")) #tuple method
print(mytuple.index("banana")) #tuple method

#now dictonary methods
student = {
    "name": "Rahul",
    "age": 21,
    "course": "CSE"
}
print(student.keys())
print(student.values())
print(student.items())
student.update({
    "city": "Delhi",
    "grade": "A"
})
student.setdefault("country", "India")

#set
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(Days)
Students = {'Monday','Alice','John','Bob','Alice'}
ss = Days.difference(Students)
print(type(Days))

#conditional
state = input('Enter your state : (GJ, DL, OT)')
age = int(input('Enter Your age : '))
percent = float(input('Enter Your percent : '))
if state == 'GJ':
    if age > 18 and percent > 60:
        print("You are eligible for gujrat")
    else:
        print("You are not eligible for gujrat")
elif state == 'DL': 
    if age > 22 and percent > 80:
        print("You are eligible for delhi")
    else:
        print("You are not eligible for delhi")
else:
    if state == 'OT' and age > 20 and percent > 80:
        print("You are eligible for other")
    else:
        print("You are eligible not for other")


#loop
n = int(input('Enter the number of rows : '))
for i in range(1, n + 1):
    print("* " * i)

#function
def multiply_list(incomes):
    
    taxes = []  # empty list to store taxes
    for income in incomes:
        tax = income * 0.20   # 20% tax
        taxes.append(tax)
    return taxes

# Example usage
income_list = [1000, 2500, 4000, 8000]
tax_list = multiply_list(income_list)

print("Incomes:", income_list)
print("20% Taxes:", tax_list)

#lamada
def x(b):
   return lambda a:a**b
sq=x(2)
cube=x(3)
print (sq(5))
print(cube(5))