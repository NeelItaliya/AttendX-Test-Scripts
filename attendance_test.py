
valid_students = [101, 102, 103]
marked_students = []


def mark_attendance(student_id):
    if student_id not in valid_students:
        return "Invalid Student ID"
    elif student_id in marked_students:
        return "Already Marked"
    else:
        marked_students.append(student_id)
        return "Attendance Marked"


# Test Case 1: Valid student
assert mark_attendance(101) == "Attendance Marked"
print("Test 1 Passed: Valid Student")

# Test Case 2: Invalid student
assert mark_attendance(999) == "Invalid Student ID"
print("Test 2 Passed: Invalid Student")

# Test Case 3: Duplicate attendance
assert mark_attendance(101) == "Already Marked"
print("Test 3 Passed: Duplicate Attendance")

print("All Attendance Tests Passed!")
