class Person:
    Name = ""
    Age = 0

    def GetData(self):
        print("Name: ",self.Name)
        print("Age: ",self.Age)


P1 = Person()
P2 = Person()

P1.Name = "John"
P1.Age = 36

P2.Name = "Jane"
P2.Age = 23


P1.GetData()