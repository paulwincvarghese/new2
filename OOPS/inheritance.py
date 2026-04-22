class Vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

#child class
class Car(Vehicle):
    def car_info(self):
        print("inside car class")

#create object of car

c1 = Car()
#acess vehicles info using car object
c1.vehicle_info()
c1.car_info()

