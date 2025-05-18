from data_fetcher import fetch_data
from animals_web_generator import generate_html
from console_printer import print_animal_info


def main():
        name = input("Enter a name of an animal: ").strip()
        animals_data = fetch_data(name)
        print_animal_info(animals_data)
        generate_html('animals.html', animals_data, name)


if __name__ == "__main__":
    main()