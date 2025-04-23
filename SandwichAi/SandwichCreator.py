import random as prob
from SandwichValues import Ingredients, IngredientsValues
#Goal, create an AI which can identify the best sandwich possible
class Sandwich:
    def __init__(self, delish, ingredients):
        self.delish = delish
        self.ingredients = []
    def AddIngredient(self, ingredients):
        self.ingredients.append(ingredients)


def CreateSandwich():
    NewSandwich = Sandwich(0, [])
    x = prob.randint(1, len(Ingredients)-1)
    for i in range(x):
        y = prob.choice(Ingredients)
        NewSandwich.AddIngredient(y)
    return NewSandwich
    






