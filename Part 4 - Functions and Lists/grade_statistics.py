# Write your solution here
def exercise_points(exercises_completed: list, exam: list):
    
    total_exercises = exercises_completed[-1] // 10
    exercise_points_converted = total_exercises + exam[-1]

    return exercise_points_converted


def grade_converted(exercise_points_converted: list, exam: list):
    #exam points 0, 20
    

    if exam[-1] < 10:
        

        return 0
    
    if exercise_points_converted < 15:
        return 0

    elif exercise_points_converted < 18:
        return 1

    elif exercise_points_converted < 21:
        return 2
    
    elif exercise_points_converted < 24:
        return 3
    

    elif exercise_points_converted < 28:
         return 4
    
    else:
         return 5    

def Statistics(grades1: list, exercises_converted:list) :
   
   #grades_statistics = grades
   #print(grades1)
   #print(exercises_converted)
   average = (sum(exercises_converted)) / len(exercises_converted)

   passed_students = sum(grades != 0 for grades in grades1)
   pass_percentage = (passed_students /len(grades1)) * 100

   print('Statistics:')
   print(f"Points average: {average:.1f}")
   print(f"Pass percentage: {pass_percentage:.1f}")
   print("Grade distribution:")
   for i in range(5, -1, -1):
        grade_count = grades1.count(i)
        print(f"{i}: {'*' * grade_count}")







def main():

    exercise_completed_list = []
    exam_points = []
    exercises_converted = []
    grades = []

    while True:

        user_input = input("Exam points and exercises completed:")

        if len(user_input) < 3:
            
            Statistics(grades, exercises_converted)
            break

        user_input = user_input.split()
        
        exam_points.append(int(user_input[0]))
        exercise_completed_list.append(int(user_input[1]))

        
        points = exercise_points(exercise_completed_list, exam_points)
        
        exercises_converted.append(points)
        
        gradesfinal =   grade_converted(points, exam_points)
        grades.append(gradesfinal)





main()