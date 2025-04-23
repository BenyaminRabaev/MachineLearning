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
# Function to save data to a JSON file
def save_to_json():
    data = {
        'IngredientsValues': IngredientsValues,
        'CondimentsValue': CondimentsValue,
        'Ingredients': Ingredients,
        'Condiments': Condiments
    }
    with open('ingredients_data.json', 'w') as f:
        json.dump(data, f, indent=4)  # Save data to 'ingredients_data.json' with indentation

# Save the data
save_to_json()
