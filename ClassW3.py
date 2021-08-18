# https://www.section.io/engineering-education/dunder-methods-python/

class Softwares:
    names = []
    versions = {}

    def __init__(self, names: list):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the names")

    def __str__(self):
        s = "The current softwares and their versions are listed below: \n"
        for key, value in self.versions.items():
            s += f"{key} : v{value} \n"
        return s

    def __setitem__(self, name, version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software Name doesn't exist")

# computer = Softwares(["Python", "R", "C++"])

class Point:
    # Waarom zou je hier x = None en y = None doen?
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        s = f'({self.x}, {self.y})'
        return s

    def __add__(self, p2):
        x = self.x + p2.x
        y = self.y + p2.y
        return Point(x, y)


# p1 = Point(1, 9)
# p2 = Point(3, 4)
#
# print(p1 + p2)
# print(p1.__add__(p2))

# Deze code begrijp ik niet
class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# rev = Reverse('SPAM')
#
# print([char for char in rev])



