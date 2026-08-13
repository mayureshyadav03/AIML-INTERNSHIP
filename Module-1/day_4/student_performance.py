name = input("Enter the name of the Student: ")

mark1 = int(input("Enter the makrs of Subject 1: "))
mark2 = int(input("Enter the marks of Subject 2: "))
mark3 = int(input("Enter the marks of Subject 3: "))

marks = [mark1, mark2, mark3]

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("\n ---STUDENT PERFORMANCE---")
print("Name: ", name)
print("Marks: ", marks)
print("Total: ", total)
print("Average: ", average)
print("Grade: ", grade)    
