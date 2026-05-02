# str=input("enter a string")
# str2=str[::-1]
# if(str==str2):
#   print("string is palindrome")
# else:
#   print("string is not palindrome")
# list=[1,3,5]  
# length=len(list)
# sum=0
# avg=0
# for el in list:
#   sum+=el
#   avg=sum/length
# print(avg)  
# leng1=int(input("enter a value"))
# list1=[]
# for val in range(leng1):
#   val=int(input("enter a value"))
#   list1.append(val)
  
# leng2=int(input("enter a value"))
# list2=[]
# for val in range(leng2):
#   val=int(input("enter a value"))
#   list2.append(val)  
  
# list=list1+list2    
# list.sort()
# for val in list:
#   print(val)
  
# tup=(1,2,3,4,5,6,7,8,9)  
# even_tuple = tuple(i for i in range(1, 21) if i % 2 == 0)
# print(even_tuple)

# odd_tuple = tuple(i for i in range(1, 21) if i % 2 != 0)
# print(odd_tuple)


# students = {}

# while True:
#     print("\nA - Add Student")
#     print("B - Update Marks")
#     print("C - Search Student")
#     print("D - Display All")
#     print("E - Exit")

    # choice = input("Enter your choice: ").upper()

    # match choice:
    #     case 'A':
    #         name = input("Enter student name: ")
    #         marks = int(input("Enter marks: "))
    #         students[name] = marks

    #     case 'B':
    #         name = input("Enter student name to update: ")
    #         if name in students:
    #             marks = int(input("Enter new marks: "))
    #             students[name] = marks
    #         else:
    #             print("Student not found")

    #     case 'C':
    #         name = input("Enter student name to search: ")
    #         if name in students:
    #             print("Marks:", students[name])
    #         else:
    #             print("Student not found")

    #     case 'D':
    #         for name, marks in students.items():
    #             print(name, ":", marks)

    #     case 'E':
    #         break

    #     case _:
    #         print("Invalid choice")
    
    
# words=["apple","banana","kiwi","cherry","mango"]
# di={}
# for val in words:
#   di[val]=len(val)
# print(di)    

# str=input("enter a string")
# count=0
# for st in str:
#   if(st==" "):
#     count+=1
# print(count)    
    
# list1=[1,2,3,4]
# list2=[5,6,7,8]    
# li1=set(list1)
# li2=set(list2)
# li=li1.union(li2)
# print(li)

# list1=[1,2,3]
# list2=[3,4]  
# li1=set(list1)
# li2=set(list2)
# li=li1.intersection(li2)
# print(li)


# str=input("enter a stirng")
# se=set()
# for s in str:
#   se.add(s)
# print(se)  
# print(len(se))

nums = [1, 2, 3, 2, 4, 5, 1, 6]

seen = set()
duplicates = set()

for i in nums:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print("Duplicate elements:", duplicates)
  
