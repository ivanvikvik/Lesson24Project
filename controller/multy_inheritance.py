class A1:
    def __init__(self, surname):
        pass

    def hello(self):
        print("A1")


class A2:
    def __init__(self, name):
        pass

class A3:
    def __init__(self, age, mark):
        pass

    def hello(self):
        print("A3")


class B(A2, A3, A1):
    def __init__(self, name, surname, age,mark, value):
        A2.__init__(name)
        A1.__init__(surname)
        A3.__init__(age, mark)


b = B()
print(B.__mro__)
b.hello()
