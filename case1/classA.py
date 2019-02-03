print('inside is imported')
class A:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def printNameNSize(self):
        print('name:{} size:{}'.format(self.name, self.size))