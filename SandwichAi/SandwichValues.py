
import json
def load_from_json():
    with open('ingredients_data.json', 'r') as f:
        data = json.load(f)  # Deserialize JSON back into Python dictionaries
    return data

# Load the data
data = load_from_json()

# Access the loaded data
IngredientsValues = data['IngredientsValues']
CondimentsValue = data['CondimentsValue']
Ingredients = data['Ingredients']
Condiments = data['Condiments']
HiddenLayer1 = data['HiddenLayer1']
HiddenLayer2 = data['HiddenLayer2']
FinalLayer = data['FinalLayer']
BiasLayer1 = data['BiasLayer1']
BiasLayer2 = data['BiasLayer2']
FinalBias = data['FinalBias']

# Function to save data to a JSON file
def save_to_json():
    data = {
        'IngredientsValues': IngredientsValues,
        'CondimentsValue': CondimentsValue,
        'Ingredients': Ingredients,
        'Condiments': Condiments,
        'HiddenLayer1': HiddenLayer1,
        'HiddenLayer2': HiddenLayer2,
        'FinalLayer': FinalLayer,
        'BiasLayer1': BiasLayer1,
        'BiasLayer2': BiasLayer2,
        'FinalBias': FinalBias
    }
    with open('ingredients_data.json', 'w') as f:
        json.dump(data, f, indent=4)  # Save data to 'ingredients_data.json' with indentation

# Save the data
save_to_json()
