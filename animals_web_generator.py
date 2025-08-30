import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animals(data):
    """Iterates through animals and prints selected fields."""
    for animal in data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "diet" in animal:
            print(f"Diet: {animal['diet']}")
        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")
        if "type" in animal:
            print(f"Type: {animal['type']}")
        print()  # blank line between animals

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    print_animals(animals_data)
