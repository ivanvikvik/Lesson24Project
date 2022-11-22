class A:
    def __init__(self, name, age=16):
        self.name = name
        self.age = age


class B(A):
    def __init__(self, name, age, mark):
        self.mark = mark
        self.age = 20
        super().__init__(name)


b = B("Alex", 30, 10)
print(b.age)

print(dir(b))
print(b.__dict__)
