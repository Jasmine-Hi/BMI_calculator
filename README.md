# BMI Calculator

A simple Python command-line program for calculating Body Mass Index (BMI).

This project allows users to enter information for multiple people, calculates each person's BMI, classifies the BMI category, and saves the results to both CSV and TXT files.

---

## Features

- Enter data for multiple people
- Validate user input
- Calculate BMI automatically
- Classify BMI category
- Save results to a CSV file
- Save results to a TXT file
- Append new records without overwriting old data

---

## BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25.0 - 29.9 | Overweight |
| 30.0 and above | Obese |

---

## Project Structure

```text
BMI_calculator/
│
├── bmi_calculator.py
├── bmi_result.csv
├── bmi_result.txt
├── README.md
└── requirements.txt
```

---

## How to Run

Clone the repository or open the project folder in VS Code.

Run the program in the terminal:

```bash
python3 bmi_calculator.py
```

or:

```bash
python bmi_calculator.py
```

---

## Example Interaction

```text
How many people would you like to enter? 3

Entering person 1 of 3
Enter your name: Jafry
Enter your weight in kg: 55
Enter your height in metres: 1.70

Information entered successfully:
Name: Jafry
BMI: 19.03
Category: normal
Jafry's information has been saved successfully.
```

---

## Example CSV Output

```csv
name,weight,height,bmi,category
Jafry,55.0,1.7,19.03,normal
Jeziy,75.0,1.88,21.22,normal
Chary,60.0,1.72,20.28,normal
```

---

## Example TXT Output

```text
Name: Jafry
Weight: 55.0 kg
Height: 1.7 metres
BMI: 19.03
Category: normal
------------------------------
```

---

## Skills Practised

This project helped me practise:

- Python functions
- User input
- if / elif / else statements
- while loops
- for loops
- try / except error handling
- Dictionaries
- CSV file writing
- TXT file writing
- Append mode
- Basic file checking with `os`
- Git and GitHub workflow

---

## Requirements

This project only uses Python built-in libraries:

- `csv`
- `os`

No external packages are required.