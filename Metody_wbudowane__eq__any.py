class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
    def __eq__(self, other):
        return any(
            (
            self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color
            )   
        )   
    pass
pass

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford2", model_name="Mustang2", top_speed=2502, color="Red2")

print(car_one == car_two)