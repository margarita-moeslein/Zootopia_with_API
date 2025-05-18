# 🐾 Animal Info Web Generator

## Overview

**Animal Info Web Generator** is a Python project that fetches animal information from the [API Ninjas Animals API](https://api-ninjas.com/api/animals) 
and generates a visually structured HTML website based on user input. The tool helps users learn about various animals' diet, habitat, and type, using real-time data from an external API.

## 🔍 Features

- Search for any animal by name (e.g., `"Fox"`, `"Monkey"`)
- Fetch up-to-date information using an external API
- Display animal data in both the terminal and a generated HTML file
- Informative error message if the animal is not found
- Lightweight and easy to run or modify

## 🛠️ Technologies Used

- **Python 3.7+**
- `requests` – to handle HTTP API requests
- `python-dotenv` – to manage your API key securely using a `.env` file
- Basic HTML/CSS template for displaying data

## 📦 Installation

1. **Clone the repository:**

   ```sh
   git clone git@github.com:margarita-moeslein/Zootopia_with_API.git
   cd Zootopia_with_API

2. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   
3. **Set up your API key:**
   Create a .env file in the project root and add your API Ninjas key:
   API_KEY=your_api_key_here

4. **Run the script:**
   ```sh
   python3 main.py
You will be prompted to enter an animal name (e.g., Fox, Elephant, Monkey).

## 🖥️ Output

   After running the script:
   Animal information will be displayed in your terminal.
   An animals.html file will be created in the same directory.
   The website will contain animal "cards" showing name, diet, location, and type.
   If the animal is not found, a friendly error message will be shown in the HTML.

## 📂 Project Structure

.
├── main.py
├── data_fetcher.py
├── animals_web_generator.py
├── console_printer.py
├── animals_template.html
├── .env
├── requirements.txt
└── README.md

## 📄 License
   This project is for educational use and part of the Masterschool bootcamp program. 
   All API usage complies with API Ninjas Terms of Use.


