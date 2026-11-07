COURSES = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business",
}

def create_student(students, username, name, age, courses=None, city="", zip_code=""):
    if username in students:
        raise ValueError(f"Username {username} already exists")

    if not isinstance(age, int) or age <= 0:
        raise ValueError(f"Age {age} is invalid and must be positive integer")

    courses = set(courses) if courses else set()
    invalid_courses = courses - COURSES

    if invalid_courses:
        raise ValueError(f"Courses {invalid_courses} are invalid and not offered by the department")

    students[username] = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": {"City": city, "Zip_code": zip_code},
    }
    return students[username]

def get_student(students, username):
    if username not in students:
        raise ValueError(f"Username {username} does not exist")
    return students[username]


def display_student(students, username):
    student = get_student(students, username)
    courses_str = ", ".join(sorted(student["courses"])) if student["courses"] else "None"
    report = (
        f"Username: {username}\n"
        f"Name: {student['name']}\n"
        f"Age: {student['age']}\n"
        f"Courses: {courses_str}\n"
        f"City: {student['address']['City']}\n"
        f"Zip_code: {student['address']['Zip_code']}"
    )
    print(report)
    return report

def display_courses(students, username):
    student = get_student(students, username)
    courses = student["courses"]
    print(f"{student['name']}'s courses: {', '.join(sorted(courses)) if courses else 'None'}")
    return courses

def display_zip(students, username):
    student = get_student(students, username)
    zip_code = student["address"]["Zip_code"]
    print(f"{student['name']}'s zip code: {zip_code}")
    return zip_code

def display_city(students, username):
    student = get_student(students, username)
    city = student["address"]["City"]
    print(f"{student['name']}'s city: {city}")
    return city


def add_course(students, username, course):
    student = get_student(students, username)

    if course not in COURSES:
        raise ValueError(f"'{course}' is not offered by the department")

    if course in student["courses"]:
        raise ValueError(f"{student['name']} is already enrolled in '{course}'")

    student["courses"].add(course)
    return student["courses"]


def remove_course(students, username, course):
    student = get_student(students, username)

    if course not in student["courses"]:
        raise ValueError(f"{student['name']} is not enrolled in '{course}'")

    student["courses"].remove(course)
    return student["courses"]


def update_course(students, username, old_course, new_course):
    student = get_student(students, username)

    if old_course not in student["courses"]:
        raise ValueError(f"{student['name']} is not enrolled in '{old_course}'")

    if new_course not in COURSES:
        raise ValueError(f"'{new_course}' is not offered by the department")

    if new_course in student["courses"]:
        raise ValueError(f"{student['name']} is already enrolled in '{new_course}'")

    student["courses"].remove(old_course)
    student["courses"].add(new_course)
    return student["courses"]


def update_student_field(students, username, field, new_value):
    student = get_student(students, username)

    if field == "age":
        if not isinstance(new_value, int) or new_value <= 0:
            raise ValueError("Age must be a positive whole number")
        student["age"] = new_value

    elif field == "name":
        if not new_value or not isinstance(new_value, str):
            raise ValueError("Name must be a non-empty string")
        student["name"] = new_value

    elif field == "city":
        student["address"]["city"] = new_value

    elif field == "zip":
        student["address"]["zip"] = new_value

    else:
        raise ValueError(f"Unknown field '{field}'. Must be one of: age, name, city, zip")

    return student

def count_students(students):
    return len(students)