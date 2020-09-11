class Animal:
    name = ""
    category = ""
    def __init__(self,name):
        self.name = name
    def set_category(self,category):
        self.category = category

class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self,animal):
        self.current_animals[animal.name]= animal.category

    def total_of_category(self,category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result+=1
        return result

class Snake(Animal):
    category ="reptile"

class Turtle(Animal):
    category="reptile"

zoo=Zoo()
turtle =Turtle("Harry")
snake = Snake("Nagini")
zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile"))
