"""
name: str
cost: int
nutrition: int
"""
class Food:
    """ Food class
    Attributes:
        name (str): name of food
        cost (int): cost of food
        nutrition (int): how nutritious it is
    """


    def __init__(self, name: str, cost: int, nutrition: int):
        """ Create a Food object.
    
    Args: 
        name: name of food
        cost: cost of food
        nutrition: how nutritious it is

        """ 
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

class Dog:
    """ Thing that goes ruff
    Attributes:
        breed (str): The dog's breed
        name (str): The dog's name
        happiness (int): The dog's happiness. Defualts to 100
    """
    def __init__(self, breed: str, name: str):
        """ Create a dog object.

        Args:
            breed: The breed of the dog
            name: name of the dog.
        """
        
        self.breed = breed
        self.name = name
        self.happiness = 100

    def __str__(self):
        return f"{self.happiness}, {self.name}"
    def eat(self, food: Food):
        """ Gets the dog to eat food.
        
        increases dogs happiness by 10% of food eaten

        Args:
            food: The food for dog to eat.
        """

        happiness_increase = food.nutrition * 0.1
        self.happiness += happiness_increase

    def bark(self):
        """ Make the dog bark
        """
        print("Ruff Ruff")

sausage = Food("Polish Sausage", 10, 100)

james = Dog("Husky", "James")

print(james)

print(james.happiness)

james.eat(sausage)
print(james.happiness)

james.bark()

"""if __name__ == "__main__":
    main()
"""
""" Encapsulation
Basic definition: protecting your object's attributes.
"""
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    def set_age(self, age: int):
        if type(age) != int:
            raise ValueError("Age must be an integer")
        self._age = age

    def age_in_5_years(self):
        return self._age + 5

    def get_age(self):
        return self._age
    
s = Student("Sally", 15)

print(s.age_in_5_years())

print(s.get_age())


