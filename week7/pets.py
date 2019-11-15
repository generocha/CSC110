'''
This program will display pet name, breed, human age and calculate the pet age
Gene Rocha
11/14/2019
'''
# Pet superclass
class Pet:
    # constructor method to create new instance
    def __init__(self, name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
    # invoke the print command
    def __repr__(self):
        return "Name: {0}, Breed: {1}, Age: {2}".format(self.name,self.breed,self.age)# return the name, breed and human age

# Dog subClass
class Dog(Pet):
    # constructor method to create new instance
    def __init__(self, name, breed, age):
        super().__init__(name,breed,age) # create a Pet object
    # check human age and return age in dog years
    def petAge(self):
        if(self.age == 1):
            self.age = 15
        elif(self.age > 2):
            self.age = (self.age - 2) * 5 + 24
        else:
            self.age = 24
        return self.age
    # invoke the print command
    def __repr__(self):
        return "{0} ({1} dog yrs)".format(super().__repr__(), self.petAge())# invoke the petAge method and return the pet age
# Cat subClass
class Cat(Pet):
    # constructor method to create new instance
    def __init__(self, name, breed, age):
        super().__init__(name,breed,age) # create a Pet object
    # check human age and return age in cat years
    def petAge(self):
        if(self.age == 1):
            self.age = 15
        elif(self.age > 2):
            self.age = (self.age - 2) * 4 + 24
        else:
            self.age = 24
        return self.age
    # invoke the petAge method and return the pet age
    def __repr__(self):
        return "{0} ({1} cat yrs)".format(super().__repr__(), self.petAge())# invoke the petAge method and return the pet age