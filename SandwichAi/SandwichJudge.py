from SandwichCreator import CreateSandwich
from SandwichValues import Ingredients, IngredientsValues
def EvaluateSandwich(Sandwich):
    DelishValue = 0
    for i in range(len(Sandwich.ingredients)):
        DelishValue = DelishValue + IngredientsValues[Sandwich.ingredients[i]]
    return DelishValue
      





