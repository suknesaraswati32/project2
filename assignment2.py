# salary=int(input("enter your salary:"))
# if salary<30000:
#   print("5%")
# if salary>=30000 and salary<=70000: 
#   print("15%") 
#   if salary>70000:
#     print("25%")
    
# a=int(input("enter a number:"))    
# b=int(input("enter another number:"))
    
# for i in range(a,b+1):
#   if i%2==0:
#     print(i)

# def count_digits(n):
#   count=0
#   while n>0:
#     count+=1
#     dig=n%10
#     n=n//10
#     print(dig)
#   print(count)
# count_digits(12345)  
  
# def sum(n):
#   sum=0
#   while n>0:
#     dig=n%10
#     sum+=dig
#     n=n//10
#   print(sum)
  
# sum(1234)  
  
# for i in range(1,101):
#    if i%3==0 and i%5==0:
#      print(i) 
  
# while True:
#   n=input("enter a number:")
#   if n=="quit":
#     break
#   elif int(n) > 0:
#     print("positive")
#   else:
#     print("negative")
  
# def calculator(a,b,op):
#   if op=="+":
#     return a+b
#   elif op=="-":
#     return a-b
#   elif op=="*":
#     return a*b
#   elif op=="/":
#     return a/b
#   else:
#     return "invalid operator"
# calculator(10,5,"+")  

def is_prime(n):
  if n<=1:
    return False
  for i in range(2,n-1):
    if n%i==0:
      return False
  return True
print(is_prime(5))

n="40"
while True:
  guess=(input("guess a number:"))
  if guess==n:
    print("correct!")
    break
  else:
    if guess<n:
      print("too low")
    else:
      print("too high")  