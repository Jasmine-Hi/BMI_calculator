import csv
import os


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi >= 30:
        return "obese"
    elif bmi >= 25:
        return "overweight"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "underweight"


def choose_number_of_people():

    while True:
        try:
            number = int(
                input("How many people would you like to enter? ")
            )

            if number <= 0:
                print("The number of people must be greater than 0.")
                continue

            return number

        except ValueError:
            print("Please enter a whole number, for example 1, 2 or 3.")


def enter_person():

    while True:
        name = input("Enter your name: ").strip()

        if name == "":
            print("Name cannot be empty. Please enter the name again.")
            continue

        try:
            weight = float(
                input("Enter your weight in kg: ")
            )

            height = float(
                input("Enter your height in metres: ")
            )

        except ValueError:
            print(
                "Invalid input. Weight and height must be numbers."
            )
            continue

        if weight <= 0 or height <= 0:
            print(
                "Weight and height must be positive numbers."
            )
            continue

        if weight >= 300:
            print(
                "The weight appears unusually high. "
                "Please check that the unit is kg."
            )
            continue

        if height >= 2.5:
            print(
                "The height appears unusually high. "
                "Please check that the unit is metres."
            )
            continue

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        person = {
            "name": name,
            "weight": weight,
            "height": height,
            "bmi": round(bmi, 2),
            "category": category
        }

        return person


def save_person_to_csv(person, filename="bmi_result.csv"):

    file_has_content = (
        os.path.exists(filename)
        and os.path.getsize(filename) > 0
    )

    fieldnames = [
        "name",
        "weight",
        "height",
        "bmi",
        "category"
    ]

    try:
        with open(
            filename,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            if not file_has_content:
                writer.writeheader()

            writer.writerow(person)

        return True

    except OSError as error:
        print(f"Failed to save the CSV file: {error}")
        return False


def save_person_to_text(person, filename="bmi_result.txt"):
    result = (
        f"Name: {person['name']}\n"
        f"Weight: {person['weight']} kg\n"
        f"Height: {person['height']} metres\n"
        f"BMI: {person['bmi']}\n"
        f"Category: {person['category']}\n"
        f"{'-' * 30}\n"
    )

    try:
        with open(
            filename,
            "a",
            encoding="utf-8"
        ) as file:
            file.write(result)

        return True

    except OSError as error:
        print(f"Failed to save the text file: {error}")
        return False


# ---------------- Main ----------------

number_of_people = choose_number_of_people()

successful_count = 0

for person_number in range(1, number_of_people + 1):

    print(
        f"\nEntering person "
        f"{person_number} of {number_of_people}"
    )

    person = enter_person()

    print("\nInformation entered successfully:")
    print(f"Name: {person['name']}")
    print(f"BMI: {person['bmi']}")
    print(f"Category: {person['category']}")

    csv_saved = save_person_to_csv(person)
    text_saved = save_person_to_text(person)

    if csv_saved and text_saved:
        successful_count += 1

        print(
            f"{person['name']}'s information "
            f"has been saved successfully."
        )

    elif csv_saved:
        print(
            "The CSV file was saved, "
            "but the text file could not be saved."
        )

    elif text_saved:
        print(
            "The text file was saved, "
            "but the CSV file could not be saved."
        )

    else:
        print(
            f"{person['name']}'s information "
            f"could not be saved."
        )


print("\nData entry completed.")
print(
    f"Successfully saved "
    f"{successful_count} of {number_of_people} people."
)


