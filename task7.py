
# Tuple-Based Course Registration Validation

# Each registration is (Student_ID, Course_Code)
registrations = [
    ("S101", "CSE101"),
    ("S101", "MAT101"),
    ("S101", "CSE101"),
    ("S102", "CSE101"),
    ("S102", "CSE201"),
    ("S103", "MAT101"),
    ("S103", "PHY101"),
    ("S104", "CSE201")
]

valid_courses = ["CSE101", "CSE201", "MAT101", "PHY101"]

# CSE101 and CSE201 cannot be taken together
invalid_combinations = [("CSE101", "CSE201")]

seen = set()
duplicates = []
invalid_records = []
student_courses = {}

# Check registrations
for student, course in registrations:

    if course not in valid_courses:
        invalid_records.append((student, course))
        continue

    if (student, course) in seen:
        duplicates.append((student, course))
        continue

    seen.add((student, course))

    if student not in student_courses:
        student_courses[student] = []

    student_courses[student].append(course)

# Check invalid course combinations
violations = {}

for student, courses in student_courses.items():
    for course1, course2 in invalid_combinations:
        if course1 in courses and course2 in courses:
            violations[student] = (course1, course2)

print("COURSE REGISTRATION AUDIT")

print("\nDuplicate Registrations:")
if duplicates:
    for item in duplicates:
        print(item)
else:
    print("None")

print("\nInvalid Course Records:")
if invalid_records:
    for item in invalid_records:
        print(item)
else:
    print("None")

print("\nStudents Violating Course Rules:")
if violations:
    for student, courses in violations.items():
        print(student, "selected incompatible courses:", courses)
else:
    print("None")

print("\nFinal Registration Status:")
all_students = sorted(set(s for s, c in registrations))

for student in all_students:
    if student in violations:
        print(student, "- Invalid course combination")
    elif any(s == student for s, c in duplicates):
        print(student, "- Duplicate registration found")
    elif any(s == student for s, c in invalid_records):
        print(student, "- Invalid course record")
    else:
        print(student, "- Valid")
