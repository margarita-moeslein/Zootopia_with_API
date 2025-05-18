from typing import Any, Dict, List


def print_animal_info(animals: List[Dict[str, Any]]) -> None:
    """Print information about each animal to the console."""
    if not animals:
        print("No animals found.")
        return

    for animal in animals:
        lines: List[str] = []
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        locations = animal.get("locations", [])

        if name:
            lines.append(f"Name: {name}")
        if "diet" in characteristics:
            lines.append(f"Diet: {characteristics['diet']}")
        if locations:
            lines.append(f"Location: {locations[0]}")
        if "type" in characteristics:
            lines.append(f"Type: {characteristics['type']}")

        print("\n".join(lines))
        print()

