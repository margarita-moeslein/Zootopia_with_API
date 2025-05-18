from typing import Any, Dict, List


# Constants
ANIMAL_HTML_TEMPLATE = "animals_template.html"
REPLACED_TEXT = "__REPLACE_ANIMALS_INFO__"


def serialize_animal(animal_data: Dict[str, Any]) -> str:
    """Convert a single animal dictionary to an HTML list item."""
    name = animal_data.get("name", "Unknown")
    characteristics = animal_data.get("characteristics", {})
    locations = animal_data.get("locations", [])

    output = f'<li class="cards__item">\n'
    output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">\n'

    if "diet" in characteristics:
        output += f'<strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
    if locations:
        output += f'<strong>Location:</strong> {locations[0]}<br/>\n'
    if "type" in characteristics:
        output += f'<strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '</p>\n</li>\n'
    return output


def generate_html(file_path: str, animals_data: List[Dict[str, Any]], animal_name: str) -> None:
    """Generate HTML output from animal data and write to a file."""
    with open(ANIMAL_HTML_TEMPLATE, 'r') as fileobj:
        template_content = fileobj.read()

    if not animals_data:
        output = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
    else:
        output = ''.join(serialize_animal(animal) for animal in animals_data)

    html_content = template_content.replace(REPLACED_TEXT, output)

    with open('animals.html', 'w') as fileobj:
        fileobj.write(html_content)

    print("Website was successfully generated to the file animals.html.")
