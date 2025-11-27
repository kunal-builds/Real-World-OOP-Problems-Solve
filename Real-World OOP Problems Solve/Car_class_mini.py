class Car:
    def __init__(self, brand, model, max_speed= 200):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.max_speed = max_speed
    
    def accelerate(self, amount=10):
        if self.speed + amount > self.max_speed:
            print(f"Cannot exeeced max speed of {self.max_speed} km/h")
        else:
            self.speed += amount
            print(f"Accelerated to {self.speed} km/h")

    def brake(self, amount=10):
        if self.speed - amount < 0:
            self.speed = 0
            print("car is now fully Stopped.")
        else:
            self.speed -= amount

    def stop(self):
        self.speed = 0
        print("car stop") 

    def show_speed(self):
        print(f"current speed: {self.speed} km/h")


car = Car("BMW", "XS")

car.show_speed()
car.accelerate()
car.accelerate(20)
car.brake()
car.stop()
car.accelerate(250)
car.show_speed()




