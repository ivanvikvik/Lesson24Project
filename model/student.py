from model.human import Human


class Student(Human):
    def __init__(self, name, surname, age, mark=4):
        print("constructor from Student class")
        super().__init__(name, surname, age)
        self.mark = mark

    def run(self):
        super().run()
        print(" to canteen...")

    def study(self):
        self.run()
        print(f"Student {self.name} is studying.")


# s1 = Student("Alex")
# print(s1.name)
# s1.run()
# s1.study()

# s2 = Student("Kate")
# print(s2.name)
# s2.run()
# s2.study()
