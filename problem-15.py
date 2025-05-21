# Problem-15: Write conditional statements to identify the student’s average marks. If any subject’s mark
# is less than 40, you should print FAILED instead of making average marks


# average_student_1 = sum(lstudent_1) / len(lstudent_1)
# if average_student_1 < 40:
#     print("FAILED")
# else:
#     print("Average marks of student_1 : ", average_student_1)

# average_student_2 = sum(student_2) / len(student_2)
# if average_student_2 < 40:
#     print("FAILED")
# else:
#     print("Average marks of student_2 : ", average_student_2)


lstudent_1 = [40, 94, 70, 90, 56, 99, 85, 77]

student_2 = [57, 65, 20, 98, 46, 99, 85, 77]


def student_Result(marks):
    if any(number < 40 for number in marks):
        return "FAILED"

    avg_Marks = sum(marks) / len(marks)
    return f"Avarage mark of the student is : {avg_Marks:.3f}"


print("Student 1 result is : ", student_Result(lstudent_1))
print("Student 2 result is : ", student_Result(student_2))





# def student_subject_average(subject_marks):
#     for marks in subject_marks:
#         if marks < 40:
#             return "FAILED"

#     avarage_marks = sum(subject_marks) / len(subject_marks)
#     return f"Avarage mark is : {avarage_marks:.2f}"


# print("Student 1 : ", student_subject_average(lstudent_1))
# print("Student 2 : ", student_subject_average(student_2))

