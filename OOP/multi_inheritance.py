class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"    

class C(A, B):

    def showprops(self):
        print(self.foo)
        print(self.bar)

    def __init__(self):
        super().__init__()
        super().__init__()

c= C()    
c.showprops()    
