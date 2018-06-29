class Car:
    def _init_(self, color, doors=4):
        self.number_of_wheels = 4
        self.color = color
        self.doors = doors

    @static_method #static methods have no context with regards to the things they touch. they do a thing it's self contained

    def honk(self):
        print("HONK!") #this be a static method, used on the object of car, don't need to know about the object to successfully honk

carl = car(('Red', 2))


if _name_== '_main_':
    car = Car('Red', 2)

we call our testing code 'main' often to make it easier to sub in testing code to make shit work

we have to tell what it means for your object to be iterable
