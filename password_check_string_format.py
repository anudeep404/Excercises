correct_password = "python123"
name = input("Enter name:")
surname = input("Enter the surname:")
password = input("Enter password:")
while correct_password != password:
    password = input("Wrong password, please enter the password again!")

print("hi %s %s you are now logged in" %(name,surname))