class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    pass
pass

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=25)

print(mustang)