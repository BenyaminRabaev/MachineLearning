
from SandwichJudge import EvaluateSandwich
from SandwichCreator import CreateSandwich
from SandwichValues import Ingredients, IngredientsValues, save_to_json
from SandwichCorrector import CorrectSandwich
from SandwichCheck import SandwichLimiter

for i in range(1000):
    SandwichLimiter(IngredientsValues)
    NewSandwich = CreateSandwich()
    SandwichRating = EvaluateSandwich(NewSandwich)
    CorrectSandwich(NewSandwich, SandwichRating)