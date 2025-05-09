
import json
def load_from_json():
    with open('WeightsAndValues.json', 'r') as f:
        data = json.load(f)  # Deserialize JSON back into Python dictionaries
    return data

# Load the data
data = load_from_json()

# Access the loaded data
HiddenLayer1 = data['HiddenLayer1']
HiddenLayer2 = data['HiddenLayer2']
FinalLayer = data['FinalLayer']
BiasLayer1 = data['BiasLayer1']
BiasLayer2 = data['BiasLayer2']
FinalBias = data['FinalBias']

# Function to save data to a JSON file
def save_to_json(HiddenLayer1, HiddenLayer2, FinalLayer, BiasLayer1, BiasLayer2, FinalBias):
    data = {

        'HiddenLayer1': HiddenLayer1,
        'HiddenLayer2': HiddenLayer2,
        'FinalLayer': FinalLayer,
        'BiasLayer1': BiasLayer1,
        'BiasLayer2': BiasLayer2,
        'FinalBias': FinalBias
    }
    with open('WeightsAndValues.json', 'w') as f:
        json.dump(data, f, indent=4) 

# Save the data
save_to_json(HiddenLayer1, HiddenLayer2, FinalLayer, BiasLayer1, BiasLayer2, FinalBias)
