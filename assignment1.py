# name=input("enter a name")
# age=int(input("enter a age"))

# print(f"hello {name}, you are {age} years old!")

# a=int(input("enter a number:"))
# b=int(input("enter another number:"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# a=int(input("enter a number:"))
# b=int(input("enter another number:"))
# c=float(input("enter a float number:"))
# a=float(a)
# b=float(b)
# print((a+b+c)/3)

# strin="45"
# print(int(strin),type(int(strin)))
# print(float(strin),type(float(strin)))
# print(str(strin),type(str(strin)))

# print(10+3*2**2)

# a=int(input("enter a number:"))
# b=int(input("enter another number:"))
# c=a
# a=b
# b=c
# print(a,b)

temp=input("enter a temperature in celsius:")
temp=float(temp)
temp_f=(temp*9/5)+32
print(f"{temp} degrees Celsius is equal to {temp_f} degrees Fahrenheit.")

r=int(input("enter a radius:"))
print(f"the area of the circle is: {3.14*r**2}")

p=int(input("enter a principal amount:"))
t=int(input("enter a time in years:"))
r=int(input("enter an interest rate:"))
p=float(p)
t=float(t)
r=float(r)
print(f"the simple interest is: {p*t*r/100}")

n=45.78
print(f"the integer part of {n} is: {int(n)}")

print(f"the fractional part of {n} is: {n-int(n)}")