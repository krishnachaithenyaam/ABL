students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Name: ")
    marks = float(input("Aggregate marks (%): "))
    subject = float(input("Minimum subject score (%): "))
    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income: "))

    if (marks >= 75 and subject >= 60
            and attendance >= 75 and income <= 300000):
        students.append((name, marks, attendance))
        print("Eligible")
    else:
        print("Not eligible")

# Rank by marks, then attendance
students.sort(key=lambda s: (s[1], s[2]), reverse=True)

print("\nScholarship Ranking")
for rank, student in enumerate(students, start=1):
    print(rank, student[0],
          "Marks:", student[1],
          "Attendance:", student[2])