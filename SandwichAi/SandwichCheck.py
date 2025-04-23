from SandwichValues import Ingredients, IngredientsValues, save_to_json

x = IngredientsValues
def SandwichLimiter(x):
    for i in range(len(x)):
        if x[Ingredients[i]]> 100:
            x[Ingredients[i]] = 100
            save_to_json
        if x[Ingredients[i]] < -200:
            x[Ingredients[i]] = -100
            save_to_json
