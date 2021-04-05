class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    def process_input(self, a, b, operation):
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
