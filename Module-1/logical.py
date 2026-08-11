age = int(input("Enter your age: "))
has_id = input("Do you have and IDcard? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote. ")
        