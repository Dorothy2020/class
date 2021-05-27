class Cow:
    
    def __init__(self, name, color, weight):
        self.name=name
        self.color=color
        self.weight=weight
    def eat(self):
        return f"The  {self.color} eats on grass"
    def walk(self):
        return f"The cow of  {self.weight} walks towards the house"
        
        