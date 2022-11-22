class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")

class C(B):
    def hello(self):
        print("C :)")


o = C()
o.hello()