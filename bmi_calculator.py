import csv

people = [
    {"name": "Alice", "weight": 50, "height": 1.68},
    {"name": "Bob", "weight": 75, "height": 1.80},
    {"name": "Cathy", "weight": 62, "height": 1.65}
]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi >= 30:
        return "obese"
    elif bmi >= 25:
        return "overweight"
    elif bmi >=18.5:
        return "normal"
    else:
        return "underweight"

try:
    name = input("Enter your name:")
    weight = float(input("Enter your weight in kg:"))
    height = float(input("Enter your height in metres: "))
    if weight <= 0 or height <= 0:
        print("weight and height must be positive number.")
    elif weight >= 300:
        print("Please note that the unit of weight is kg")
    elif height >= 2.5:
        print("please note that height is measured in metres")
    else:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        person = {
            "name": name,
            "weight": weight,
            "height": height,
            "BMI": round(bmi,2),
            "category": category
        }
        people.append(person)
        
        result = f"Name: {name}\nBMI:{bmi:.2f}\nCategory:{category}"
        print(result)
        
        with open("bmi_result.txt", "w") as f:
            f.write(result)
        
        with open("bmi_result.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            
            writer.writerow(["name","weight", "height", "bmi", "category"])
            
            writer.writerow([
                person["name"],
                person["weight"],
                person["height"],
                person["BMI"],
                person["category"]
            ])
        print("BMI result saved to bmi_result.csv")
        
        with open("bmi_result.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(["name","weight", "height", "bmi", "category"])
            writer.writerow([name, weight, height, round(bmi, 2), category])

except ValueError:
    print("Please enter number only.")


