# class Person:
#     def get_age(self) -> int:
#         raise NotImplementedError()


# class Worker(Person):
#     def get_age(self) -> int:
#         return 15


# class Player(Person):
#     pass


# worker = Worker()

# print(worker.get_age())


# MRO - Method Resolution Order
class A:
    def foo(self) -> None:
        print("A.foo")


class B(A):
    def foo(self) -> None:
        print("B.foo")


class C(A):
    def foo(self) -> None:
        print("C.foo")


class D(B, C):
    pass


d = D()
d.foo()  # prints "B.foo"
print(D.__mro__)
