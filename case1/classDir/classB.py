from ..classA import A

class B(A):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def printColor(self):
        print('color:{}'.format(self.color))