class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Tạo một thể hiện mới")
        instance = super(MyClass, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print("Khởi tạo thể hiện")
        self.value = value

# obj = MyClass(10)
import requests

class IntClass:
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return int(self.value)

# obj = IntClass(3.14)
# result = int(obj)
# print(result)


class ContainerClass:
    def __init__(self, values):
        self.values = values

    def __contains__(self, item):
        return item in self.values

obj = ContainerClass([1, 2, 3, 4, 5])
# print(3 in obj)





class CallableClass:
    def __call__(self, x):
        return x * x

obj = CallableClass()

result = obj(5)

# print(result)  



class EqClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

obj1 = EqClass(42)
obj2 = EqClass(42)
# print(obj1 == obj2)




class BoolClass:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value > 0

obj = BoolClass(42)
# print(bool(obj)) 



class AddClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return AddClass(self.value + other.value)

obj1 = AddClass(10)
obj2 = AddClass(20)
result = obj1 + obj2
# print(result.value)  



class NeClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

obj1 = NeClass(42)
obj2 = NeClass(42)
print(obj1 != obj2) 
