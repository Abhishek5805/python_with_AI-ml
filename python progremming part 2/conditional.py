# color=input("enter the color of traffic light")

# if color=="red":
#     print("stop")
# elif color=="yellow":
#     print("ready")
# else:
#     print("go")


# username=input("enter the username")
# password=input("enter the password")

# if username=="abhi" and password=="123":
#     print("login successful")
# else:
#     if(username!="abhi"):
#         print("invalid username")
#     else:
#         print("invalid password")



# count=1

# while count<=5:
#     print("count is",count)
#     count+=1

salary=float(input("enter the salary"))

if salary<=30000:
    tax=salary*0.05
elif salary<=70000:
    tax=salary*0.15
else:
    tax=salary*0.25

final_salary=salary-tax

print("original salary is",salary)
print("the final salary after tax deduction is",final_salary)
print("the tax amount is",tax)