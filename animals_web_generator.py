import json


def load_data(file_path):
    """Load JSON file containing animal data."""
    with open(file_path, "r") as f:
        return json.load(f)


def serialize_animal(animal_obj):
    """Serialize a single animal object into HTML using nested <ul>."""
    output = '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f"  <div class='card__title'>{animal_obj['name']}</div>\n"

    output += "  <div class='card__text'>\n    <ul class='card__fields'>\n"

    # Diet
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f"      <li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n"

    # Locations
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        locations_str = ", ".join(animal_obj["locations"])
        output += f"      <li><strong>Location:</strong> {locations_str}</li>\n"

    # Type
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f"      <li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>\n"

    # Skin Type
    if "characteristics" in animal_obj and "skin_type" in animal_obj["characteristics"]:
        output += f"      <li><strong>Skin Type:</strong> {animal_obj['characteristics']['skin_type']}</li>\n"
    else:
        output += f"      <li><strong>Skin Type:</strong> Unknown</li>\n"

    output += "    </ul>\n  </div>\n</li>\n"
    return output


def generate_animals_html(data):
    """Generate HTML for all animals by serializing each one."""
    # Sort alphabetically by name
    sorted_data = sorted(data, key=lambda x: x.get("name", ""))
    return "".join(serialize_animal(animal) for animal in sorted_data)


def create_html_page(animals_html):
    """Return the full HTML page as a string."""
    return f"""
<html>
<head>
  <meta charset="UTF-8">
  <title>My Animal Repository</title>
  <style>
    html {{ background-color: #ffe9e9; }}
    body {{
      font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
      padding: 1rem;
      width: 900px;
      margin: auto;
    }}
    h1 {{
      text-align: center;
      font-size: 40pt;
      font-weight: normal;
    }}
    .cards {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .cards__item {{
      background-color: white;
      border-radius: 0.25rem;
      box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
      overflow: hidden;
      padding: 1rem;
      margin: 50px 0;
    }}
    .card__title {{
      font-size: 1.25rem;
      font-weight: 300;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }}
    .card__text {{
      font-size: 0.95rem;
      line-height: 1.5;
    }}
    .card__fields {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .card__fields li {{
      padding: 2px 0;
    }}
  </style>
</head>
<body>
  <h1>My Animal Repository</h1>
  <ul class="cards">
    {animals_html}
  </ul>
</body>
</html>
"""


def main():
    data = load_data("animals_data.json")
    animals_html = generate_animals_html(data)
    full_html = create_html_page(animals_html)

    with open("animals.html", "w") as f:
        f.write(full_html)

    print(f"HTML file generated with {len(data)} animals.")


if __name__ == "__main__":
    main()
