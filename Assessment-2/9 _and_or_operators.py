age = int(input("Enter your age: "))
member = input("Are you a member? (yes/no): ")

if age >= 18 and member == "yes":
    print("Full Access Granted")

elif age >= 18 or member == "yes":
    print("Limited Access Granted")

else:
    print(" Access Denied")


