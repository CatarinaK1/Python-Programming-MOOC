# Please write a program which asks for the number of students on a course and the desired group size. 

# The program will then print out the number of groups formed from the students on the course. 
# If the division is not even, one of the groups may have fewer members than specified.

students_in_course = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))

groups = students_in_course  // desired_group_size 
leftover = students_in_course % desired_group_size 

if leftover > 0:
    groups += 1


print(f"Number of groups formed: {groups}")