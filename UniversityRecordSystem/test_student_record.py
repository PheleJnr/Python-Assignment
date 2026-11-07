import unittest
from student_record import (
    create_student,
    display_student,
    display_courses,
    display_zip,
    display_city,
    add_course,
    remove_course,
    update_course,
    update_student_field,
    count_students

)


class TestCreateStudent(unittest.TestCase):
    def test_that_new_student_record_can_be_created_successfully(self):
        self.student = {}
        create_student(self.student, "PheleJnr96", "Matthew Ayobami",16,
                       courses={"Math", "Physics", "Chemistry"}, city= "Lagos", zip_code= "100001")

        self.assertIn("PheleJnr96", self.student)
        self.assertEqual((self.student["PheleJnr96"]["name"]), "Matthew Ayobami")
        self.assertEqual((self.student["PheleJnr96"]["age"]), 16)

    def test_that_new_student_record_can_be_created_with_empty_courses_successfully(self):
        self.student = {}
        create_student(self.student, "PheleJnr96", "Matthew Ayobami",16,)
        self.assertEqual((self.student["PheleJnr96"]["courses"]), set())

    def test_that_new_student_record_created_raises_error_with_duplicates_usernames_successfully(self):
        self.student = {}
        create_student(self.student, "PheleJnr96", "Matthew Ayobami",16,)
        with self.assertRaises(ValueError):
            create_student(self.student, "PheleJnr96", "Matthew Adegoke",18,)

    def test_that_new_student_record_created_raises_error_with_invalid_age_successfully(self):
        self.student = {}
        with self.assertRaises(ValueError):
            create_student(self.student, "PheleJnr96", "Matthew Ayobami", -16)

    def test_that_new_student_record_created_raises_error_with_non_integer_age_successfully(self):
        self.student = {}
        with self.assertRaises(ValueError):
            create_student(self.student, "PheleJnr96", "Matthew Ayobami", "twenty-two")

    def test_unoffered_course_at_creation_raises(self):
        self.student = {}
        with self.assertRaises(ValueError):
            create_student(self.student, "PheleJnr96", "Matthew Ayobami", 16, courses={"Astrology"})

class TestDisplayStudentRecords(unittest.TestCase):
    def setUp(self) -> None:
        self.student = {}
        create_student(self.student, "PheleJnr96", "Matthew Ayobami", 16,
                       courses={"Math", "Physics", "Chemistry"}, city="Lagos", zip_code="100001"
                       )

    def test_that_when_new_student_record_created_display_student_returns_content_successfully(self):
        report = display_student(self.student, "PheleJnr96")
        self.assertIn("PheleJnr96", report)
        self.assertIn("Matthew Ayobami", report)
        self.assertIn("Physics", report)

    def test_that_when_new_student_record_created_display_student_raises_error_when_missing_username(self):
        with self.assertRaises(ValueError):
            display_student(self.student, "PheleJnr")

    def test_that_when_new_student_record_created_display_courses_returns_correct_set(self):
        courses = display_courses(self.student, "PheleJnr96")
        self.assertEqual(courses, {"Math", "Chemistry", "Physics"})

    def test_that_when_new_student_record_created_display_zip_returns_correct_value(self):
        self.assertEqual(display_zip(self.student, "PheleJnr96"), "100001")

    def test_that_when_new_student_record_created_display_city_returns_correct_value(self):
        self.assertEqual(display_city(self.student, "PheleJnr96"), "Lagos")

    def test_that_when_new_student_record_created_display_courses_raises_error_when_missing_student(self):
        with self.assertRaises(ValueError):
            display_courses(self.student, "Phantom")

class TestAddCourse(unittest.TestCase):
    def setUp(self) -> None:
        self.student = {}
        create_student(self.student, "PheleJnr96", "Matthew Ayobami", 16,
                       courses={"Math", "Physics", "Chemistry"}, city="Lagos", zip_code="100001"
                       )

    def test_that_when_new_student_record_created_add_new_valid_course(self):
        result = add_course(self.student, "PheleJnr96", "Biology")
        self.assertEqual(result, {"Math", "Chemistry", "Physics", "Biology"})

    def test_that_when_new_student_record_created_adding_duplicate_course_raises_error(self):
        with self.assertRaises(ValueError):
            add_course(self.student, "PheleJnr96", "Math")

    def test_that_when_new_student_record_created_adding_unoffered_course_raises_error(self):
        with self.assertRaises(ValueError):
            add_course(self.student, "PheleJnr96", "Banking")

    def test_that_when_new_student_record_created_add_course_missing_student_raises(self):
        with self.assertRaises(ValueError):
            add_course(self.student, "PheleJnr96", "Math")


class TestRemoveAndUpdateCourse(unittest.TestCase):

    def setUp(self) -> None:
        self.student = {}
        create_student(self.student, "PheleJnr96", "Matthew Ayobami", 16,
                       courses={"Math", "Physics", "Chemistry"}, city="Lagos", zip_code="100001"
                       )

    def test_that_when_new_student_record_created_and_courses_has_been_added_remove_existing_course(self):
        result = remove_course(self.student, "PheleJnr96", "Math")
        self.assertEqual(result, {"Physics", "Chemistry"})

    def test_that_when_new_student_record_created_and_courses_has_been_added_remove_courses_not_enrolled_raises_error(self):
        with self.assertRaises(ValueError):
            remove_course(self.student, "PheleJnr96", "Biology")

    def test_that_when_new_student_record_created_and_courses_has_been_added_update_courses_replaces_correctly(self):
        result = update_course(self.student, "PheleJnr96", "Math", "Biology")
        self.assertEqual(result, {"Physics", "Chemistry", "Biology"})

    def test_that_when_new_student_record_created_and_courses_has_been_added_updating_course_old_course_not_enrolled_raises_error(self):
        with self.assertRaises(ValueError):
            update_course(self.student, "PheleJnr96", "Biology", "Chemistry")

    def test_that_when_new_student_record_created_and_courses_has_been_added_update_course_new_course_not_offered_raises_error(self):
        with self.assertRaises(ValueError):
            update_course(self.student, "PheleJnr96", "Math", "Astrology")

    def test_that_when_new_student_record_created_and_courses_has_been_added_update_course_new_course_already_enrolled_raises_no_duplicate(self):
        with self.assertRaises(ValueError):
            update_course(self.student, "PheleJnr96", "Math", "Physics")
        self.assertEqual(self.student["PheleJnr96"]["courses"], {"Math", "Physics", "Chemistry"})

class TestUpdateStudentField(unittest.TestCase):

    def setUp(self):
        self.student = {}
        create_student(
            self.student, "PheleJnr96", "Matthew Ayobami", 16, city= "Lagos", zip_code= "100001",
        )

    def test_that_new_student_record_has_been_created_and_we_update_the_student_age(self):
        update_student_field(self.student, "PheleJnr96", "age", 28)
        self.assertEqual(self.student["PheleJnr96"]["age"], 28)

    def test_that_new_student_record_has_been_created_and_updating_an_invalid_student_age_raises_error(self):
        with self.assertRaises(ValueError):
            update_student_field(self.student, "PheleJnr96", "age", -1)

    def test_that_new_student_record_has_been_created_and_we_update_the_student_name(self):
        update_student_field(self.student, "PheleJnr96", "name", "M Ayobami")
        self.assertEqual(self.student["PheleJnr96"]["name"], "M Ayobami")

    def test_that_new_student_record_has_been_created_and_updating_a_student_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            update_student_field(self.student, "PheleJnr96", "name", "")

    def test_that_new_student_record_has_been_created_and_we_update_the_student_city(self):
        update_student_field(self.student, "PheleJnr96", "city", "Abuja")
        self.assertEqual(self.student["PheleJnr96"]["address"]["city"], "Abuja")

    def test_that_new_student_record_has_been_created_we_update_the_student_zip_code_address(self):
        update_student_field(self.student, "PheleJnr96", "zip", "900001")
        self.assertEqual(self.student["PheleJnr96"]["address"]["zip"], "900001")

    def test_that_new_student_record_has_been_created_updating_unknown_field_raises_error(self):
        with self.assertRaises(ValueError):
            update_student_field(self.student, "PheleJnr96", "grade", "A")

    def test_that_new_student_record_has_been_created_and_updating_the_field_missing_student_raises_error(self):
        with self.assertRaises(ValueError):
            update_student_field(self.student, "Phantom", "age", 20)


class TestCountStudents(unittest.TestCase):

    def setUp(self):
        self.student = {}

    def test_that_no_student_record_has_been_created_count_zero_students(self):
        self.assertEqual(count_students(self.student), 0)

    def test_that_new_student_record_has_been_created_count_after_adding_students(self):
        create_student(self.student, "user1", "Student One", 20)
        create_student(self.student, "user2", "Student Two", 21)
        self.assertEqual(count_students(self.student), 2)

    def test_that_new_student_record_has_been_created_count_unaffected_by_course_changes(self):
        create_student(self.student, "user1", "Student One", 20, courses={"Math"})
        add_course(self.student, "user1", "Biology")
        self.assertEqual(count_students(self.student), 1)


if __name__ == '__main__':
    unittest.main()
