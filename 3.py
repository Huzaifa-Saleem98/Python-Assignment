print("Qno 1")
user=int (input("Enter your age here:"))
if user<0:
        print("Invalid age. Age cant be negative !")
elif user<=12:
     print ("Category: Child !")
elif 13<=user<=19:
    print("Category: Teen Age")
elif 20<=user<=59:
    print("Category: Adult")
else:
    print("Category: Senior")
    

print("Qno 2")
num=int(input("Enter your number here, and find the type of your number:"))
if num<0:
     print("Your number is NEGATIVE !")
elif num==0:
    print("Your number is ZERO !")
elif num>0:
     print("Your number is POSITIVE !")

print("Qno 3")

numbers=[10,20,30,40,50]
print("Numbers in the list are:")
for number in numbers:
     print(number)
print("Last item in the list is:")
print(numbers[-1])

print("Qno 4")
student={
    "name":"Huzaifa",
    "city":"Karachi",
    "age":18
}
print(student)
print("Now after update:")
student.update({"Roll no":25})
print(student.keys())
print(student.values())
print(student.items())
print("Assignment Completed !")