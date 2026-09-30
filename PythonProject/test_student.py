import unittest

from student import Student

class TestStudent(unittest.TestCase):
    def test_that_student_can_be_created_by_name_and_grade(self):
        pupil = Student("Matthew", 1)
        self.assertEqual(pupil.name, "matthew")
        self.assertEqual(pupil.grade_level, 1)

    def test_that_student_grade_level_cannot_be_less_than_the_min_grade_level(self):
        with self.assertRaises(ValueError):
            Student("Matthew", -2)

    def test_that_student_grade_level_cannot_be_greater_than_the_max_grade_level(self):
        with self.assertRaises(ValueError):
            Student("Matthew", 13)

    def test_that_student_grade_level_accepts_boundaries(self):
        self.assertEqual(Student("Matthew", 1).grade_level, 1)
        self.assertEqual(Student("Matthew", 12).grade_level, 12)


    def test_that_student_can_be_introduced_by_name_and_by_grade(self):
        message = Student("Matthew", 8).introduce()
        self.assertIn("matthew", message)
        self.assertIn("8", message)

    def test_that_student_can_be_promoted_up_by_one_grade_level(self):
        pupil = Student("Matthew", 1)
        pupil.promote()
        self.assertEqual(pupil.grade_level, 2)

    def test_that_student_can_be_promoted_up_to_the_final_grade_level(self):
        pupil = Student("Matthew", 11)
        pupil.promote()
        self.assertEqual(pupil.grade_level, 12)

    def test_that_student_cannot_be_promoted_above_the_final_grade_level(self):
        pupil = Student("Matthew", 12)
        with self.assertRaises(ValueError):
            pupil.promote()
        self.assertEqual(pupil.grade_level, 12)

    def test_that_student_passed_the_average_score(self):
        pupil = Student("Matthew", 1)
        self.assertTrue(pupil.has_passed(75))

    def test_that_student_scores_below_passing_scores_does_not_pass(self):
        pupil = Student("Matthew", 1)
        self.assertFalse(pupil.has_passed(30))

    def test_that_student_can_update_their_name_to_new_name(self):
        pupil = Student("matthew", 10)
        pupil.update_name("joshua")
        self.assertEqual("joshua", "joshua")

    def test_that_student_in_final_grade_can_graduate(self):
        pupil = Student("Matthew", 12)
        self.assertTrue(pupil.is_graduating())

    def test_that_student_can_not_graduate_when_not_in_final_grade_level(self):
        pupil = Student("Matthew", 5)
        self.assertFalse(pupil.is_graduating())

if __name__ == '__main__':
    unittest.main()
