def calculate_grade():
    print("Enter marks of Physics, Chemistry, Maths, English, Biology in order: ")
    marks = input()
    try:
        mark_list = [int(i) for i in marks.split()]
        avg_mark = int(sum(mark_list)/len(mark_list))
    except ValueError:
        print("You should input a number as your mark")
        return

    print(f"Your avg score is: {avg_mark}")

    if avg_mark >= 90:
        print("Your grade is: A+")
        return "A+"
    elif  avg_mark >= 80 and avg_mark < 90:
        print("your grade is: A")
        return "A"
    elif avg_mark >=70 and avg_mark < 80:
        print("your grade is: B+")
        return "B+"
    elif avg_mark >= 60 and avg_mark < 70:
        print(" Your grade is: B")
        return "B"
    elif avg_mark >= 50 and avg_mark < 60:
        print("your grade is: C+")
        return "C+"
    elif avg_mark >= 45 and avg_mark < 50:
        print("YOur grade is:  C")
        return "C"
    else:
        print("You are failed")
        return "D"



if __name__ == "__main__":
    calculate_grade()