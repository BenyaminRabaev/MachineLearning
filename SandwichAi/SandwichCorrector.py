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
            IngredientsValues[Sandwich.ingredients[i]] = IngredientsValues[Sandwich.ingredients[i]] + random.randint(1,20)/10
            save_to_json()
    if SandwichRating == 50:
        save_to_json
            
    if SandwichRating < 51:
        for i in range (len(Sandwich.ingredients)-1):
            IngredientsValues[Sandwich.ingredients[i]] = IngredientsValues[Sandwich.ingredients[i]] - random.randint(1,20)/100
            save_to_json()

            

CorrectSandwich(Sandwich, SandwichRating)







