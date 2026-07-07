# list=[1,2,3,4,5]

# sum=0
# for i in list:
#     sum+=i

# average=sum/len(list)
# print("The average of the list is:", average)


##3

# num1=list(map(int,input("Enter the numbers:").split()))
# num2=list(map(int,input("Enter the numbers:").split()))

# result=num1+num2

# print("The merged list is:", result)

# sorted_list=sorted(result)
# print("The sorted list is:", sorted_list)

#4
# tupple1=(1,2,3,4,5)

# even=[]
# odd=[]
# for i in tupple1:
    
#     if i%2==0:
#         even.append(i)
        
#     else:
#         odd.append(i)
    

# print("The number of even numbers in the tuple is:", even)
# print("The number of odd numbers in the tuple is:", odd)

#5
# dict={

# }

# print("enter A for add student")
# print("enter B for update the marks")
# print("enter C for seaarch the student")
# print("enter D for display the student")
# choice=input("Enter your choice:")
# match choice:

#     case "A":
#         name=input("Enter the name of the student:")
#         marks=int(input("Enter the marks of the student:"))
#         dict[name]=name
#         dict[marks]=marks
#         print("Student added successfully.")

#     case "B":
#         name=input("Enter the name of the student to update marks:")
#         if name==dict["name"]:
#             marks=int(input("Enter the new marks:"))
#             dict["marks"]=marks
#             print("Marks updated successfully.")
#         else:
#             print("Student not found.")
    
#     case "C":
#         name=input("Enter the name of the student to search:")
#         if name==dict["name"]:
#             print("Student found. Name:", dict["name"], "Marks:", dict["marks"])
#         else:
#             print("Student not found.")

#     case "D":
#         print("Student details. Name:", dict["name"], "Marks:", dict["marks"])


words = ["apple", "banana", "kiwi", "cherry", "mango"]

modified_words={}

for word in words:
    
    modified_words[word] = len(word)    

print("Modified words:", modified_words)