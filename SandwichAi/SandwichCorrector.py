import random
from SandwichJudge import EvaluateSandwich
from SandwichCreator import CreateSandwich
from SandwichValues import Ingredients, IngredientsValues, save_to_json
import json

Sandwich = CreateSandwich()
SandwichRating = EvaluateSandwich(Sandwich)


def CorrectSandwich(Sandwich, SandwichRating):
    if SandwichRating > 49:
        for i in range (len(Sandwich.ingredients)-1):
            IngredientsValues[Sandwich.ingredients[i]] = IngredientsValues[Sandwich.ingredients[i]] + random.randint(1,200)/10
            print(IngredientsValues)
    if SandwichRating < 51:
        for i in range (len(Sandwich.ingredients)-1):
            IngredientsValues[Sandwich.ingredients[i]] = IngredientsValues[Sandwich.ingredients[i]] - random.randint(1,200)/100
            print(IngredientsValues)

CorrectSandwich(Sandwich, SandwichRating)







