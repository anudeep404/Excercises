correct_password = "python123"
password = input("Enter password:")
while correct_password != password:
    password = input("Wrong password, please enter the password again!")

print("Logged IN")