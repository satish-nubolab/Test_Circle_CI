class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        return 'hello world'

    def process_input(self, a, b, operation):
        print("::::::::::", a, b, operation)
        if operation == "add":
            return a + b
        if operation == "subtract":
            return a - b
        if operation == "multiple":
            return a * b
        if operation == "divide":
            if b == 0:
                return "Invalid Input"
            return a / b
