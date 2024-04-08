class Parent1:
    def __init__(self):
        # print('Parent1.__init__')
        self.value = 5
    
    def get_value(self):
        # print('Parent1.get_value')
        return self.value

class Child1(Parent1):
    def __init__(self):
        # print('Child1.__init__')
        self.value = 10
        super().__init__()
    
    def get_value(self, *args): # *args: tuple
        return self.value + 15
    
child = Child1()
a = child.get_value()
print(a)