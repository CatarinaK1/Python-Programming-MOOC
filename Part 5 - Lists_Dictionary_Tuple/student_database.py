
def add_student(students: dict, name: str):

    if name not in students:

        students[name] = []

    return students

def print_student(students: dict, name: str):

    if name in students:
        courseGrade = 0

        if students[name]:
            print(f"{name}: \n {len(students[name])} completed courses:")

            for course, grade in students[name]:
                print(f"  {course} {grade}")
                courseGrade += grade
            courseGrade = courseGrade / len(students[name])

            print(f" average grade {courseGrade}")


        else:
            print(f"{name}: \n no completed courses")
     
    else:

        print(f"{name}: no such person in the database")
    # for studentName, studentInfo in students.items():

def add_course(students: dict, name: str, courseName_and_Grade: tuple):

    CourseName, CourseGrade = courseName_and_Grade

    if name in students:

        if CourseName in [course for course, _ in students[name]]:
            # enumerate function is a built-in Python function that returns both the index and the value from an iterable.
            for i, (course, grade) in enumerate(students[name]):

                if course == CourseName:
                    students[name][i] = (CourseName, max(CourseGrade, grade))
                    break

        elif CourseGrade > 0:
            students[name].append(courseName_and_Grade)


def summary(students: dict):

    most_courses = 0
    best_average = 0


    for name in students:

        if len(students[name])  > most_courses:
            most_courses, most_courses_student = len(students[name]), name


 
        average_grade = sum(grade for _, grade in students[name]) / len(students[name])

        if average_grade > best_average:
            best_average = average_grade
            best_average_student = name
    
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses} {most_courses_student}")
    print(f"best average grade {best_average} {best_average_student}")




if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")


    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")

    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")

    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))

    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    summary(students)