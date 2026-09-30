class Student:
    MIN_GRADE_LEVEL = 1
    MAX_GRADE_LEVEL = 12
    PASSING_SCORE = 50

    def __init__(self, name: str, grade_level: int) -> None:
        self.name = name.lower()
        self.grade_level = grade_level
        self.validate_grade_level()


    def validate_grade_level(self) -> None:
        if self.grade_level < self.MIN_GRADE_LEVEL:
            raise ValueError ("Invalid grade level")
        elif self.grade_level > self.MAX_GRADE_LEVEL:
            raise ValueError ("Invalid grade level")


    def introduce(self):
        message = f"Hi, I'm {self.name} and I'm in grade {self.grade_level}."
        print(message)
        return message

    def promote(self):
        if self.grade_level >= self.MAX_GRADE_LEVEL:
            raise ValueError ("Student is already in the final grade level")
        self.grade_level += 1

    def has_passed(self, score) -> bool:
        return score >= self.PASSING_SCORE

    def update_name(self, new_name: str) -> None:
        self.name = new_name

    def is_graduating(self)-> bool | None:
        if self.grade_level == self.MAX_GRADE_LEVEL:
            return True



