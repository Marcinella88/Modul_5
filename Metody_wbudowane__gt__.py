class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
    def __eq__(self, other):
        return (
            self.make == other.make and
            self.model_name == other.model_name and
            self.top_speed == other.top_speed and
            self.color == other.color            
        )
    def __gt__(self, other):
        return self.top_speed > other.top_speed   
    pass
pass

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")

car_three = Car(make="Ford", model_name="Mustang", top_speed=260, color="Yellow")

print(car_one == car_two)
print(car_one == car_three)
print(car_one > car_three)