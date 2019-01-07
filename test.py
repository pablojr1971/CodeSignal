class A(object):
    def __init__(self):
        print ("world")

class B(A):
    def __init__(self):
        print ("hello")
        super(B, self).__init__()

A()

class Person: 
    def __init__(self, name, job=None, pay=0): 
        self.name = name 
        self.job = job 
        self.pay = pay 

if __name__ == '__main__': # When run for testing only # self-test code 
    bob = Person('Bob Smith') 
    sue = Person('Sue Jones', job='dev', pay=100000) 
    print(bob.name, bob.pay) 
    print(sue.name, sue.pay)