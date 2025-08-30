import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animals_string(data):
    """Generates a string with animals' info."""
    output = ""
    for animal in data:
        if "name" in animal:
            output += f"Name: {animal['name']}\n"
        if "diet" in animal:
            output += f"Diet: {animal['diet']}\n"
        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}\n"
        if "type" in animal:
            output += f"Type: {animal['type']}\n"
        output += "\n"  # blank line between animals
    return output

def main():
    # Step 1: Load data
    animals_data = load_data("animals_data.json")

    # Step 2: Generate animals info string
    animals_string = generate_animals_string(animals_data)

    # Step 3: Read template
    with open("animals_template.html", "r") as f:
        template = f.read()

    # Step 4: Replace placeholder
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

    # Step 5: Write new HTML file
    with open("animals.html", "w") as f:
        f.write(new_html)

if __name__ == "__main__":
    main()
