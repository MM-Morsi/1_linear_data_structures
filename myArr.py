# creating an array
class myArr:
    def __init__(self, capacity = 5):
        self.length = 0
        self.data = {}
        self.capacity = capacity
    def __str__(self):
        return str(self.__dict__)
    def add(self, item):
        self.data[self.length] = item
        self.length += 1
        if self.length == self.capacity:
            self.resize()
    def resize(self):
        self.capacity *= 2


arr1 = myArr()
print(arr1)

arr1.add(5)
print(arr1)

arr1.add(10)
print(arr1)