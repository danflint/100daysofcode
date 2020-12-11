"""
BMI calculator - body mass index calculator.
BMI pattern = mass(in kilograms)/height(in meters) power 2
"""

# 0:   < 15
# 1:   > 15 and < 16
# 2:   > 16 and < 18.5
# 3:   > 18.5 and < 25
# 4:   > 25 and < 30
# 5:   > 30 and < 35
# 6:   > 35 and < 40
# 7:   > 40  
bmi_category = {
    0: "Very severely underweight",
    1: "Severely underweight",
    2: "Underweight",
    3: "Normal",
    4: "Overweight",
    5: "Obese Class I",
    6: "Obese Class II",
    7: "Obese Class III",
}


def bmi_assessment(bmi):
    if bmi < 15:
        return bmi_category[0]
    elif bmi > 15 and bmi < 16:
        return bmi_category[1]
    elif bmi > 16 and bmi < 18.5:
        return bmi_category[2]
    elif bmi > 18.5 and bmi < 25:
        return bmi_category[3]
    elif bmi > 25 and bmi < 30:
        return bmi_category[4]
    elif bmi > 30 and bmi < 35:
        return bmi_category[5]
    elif bmi > 35 and bmi < 40:
        return bmi_category[6]
    else:
        return bmi_category[7]

def bmi_checker():
    print("Welcome in BMI calculator.")
    user_weight = float(input("Type yuor weight in kilograms.\n"))
    user_height = float(input("Type your height in meters\n"))
    bmi = round(user_weight / user_height**2, 2)
    category = bmi_assessment(bmi)
    print(f"Your BMI is equal to {bmi} and your are in {category} category.")

bmi_checker()
