#In this programme i understood how indexing works 
'''
fruits = ["apple", "banana", "cherry", "mango"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
'''

#Now we will print the below conditions of slicing
'''
fruits = ["apple", "banana", "mango", "orange", "grapes"]

print(fruits[:3])
print(fruits[3:])
print(fruits[1:4])
print(fruits[1:4])
'''

#Now we will se how the modifing in the list is done 

'''
heroes = ["spiderman", "thor", "hulk", "ironman", "captain america"]

heroes.append("doctor strange")
print(heroes)
heroes.insert(1, "black panthar")
print(heroes)
heroes.remove("thor")
print(heroes)
heroes.pop(3)
print(heroes)
'''

#Here i will write a programme for reversing and sorting 

'''
heroes = ["spiderman", "thor", "hulk", "ironman", "captain america"]

heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
'''

#here we will do the task

programming_language = ["Python", "Java", "C", "HTML", "R"]

for PL in programming_language:
    print(PL)

for PL in programming_language:
    if PL == "Python":
        print("Python -> I am Learning this ")
    else:
        print(f"{PL} -> Another programming language")
                