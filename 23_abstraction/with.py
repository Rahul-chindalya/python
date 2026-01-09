from abc import ABC,abstractmethod

class Laptop():
    @abstractmethod
    def key():
        pass
    @abstractmethod
    def power():
        pass

class Dell(Laptop):
    def key():
        print("lully")
    def power():
        print("cut lully")

d= Dell()

