class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет."

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age


class Student(Person):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group

    def introduce(self):
        return f"Меня зовут {self.name}, я учусь в группе {self.group}."


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Меня зовут {self.name}, я преподаю предмет {self.subject}."


def show_introduction(person):
    print(person.introduce())


def main():
    student = Student("Анна", 20, "Python-1")
    teacher = Teacher("Игорь", 35, "Django")
    another_student = Student("Олег", 20, "Python-2")

    show_introduction(student)
    show_introduction(teacher)

    print(student)
    print("Одинаковый возраст:", student == another_student)


if __name__ == "__main__":
    main()
