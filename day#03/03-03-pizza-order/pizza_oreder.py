"""
Order pizza. Avaliable things:
Size: S,M,XL  Price: 15, 20, 25
Peperoni S: +2
Pepperoni M, XL +3
Extra cheese: +1
"""

pizza_data = {
    's': 14.99,
    'm': 20.99,
    'xl': 24.99,
    'pepperoni': 
    {
        's': 2,
        'm': 3,
        'xl': 3,
    },
    'extra_cheese':
    {
        'y': 1,
        'n': 0,
    },
}

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, XL")
add_peperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

summary = pizza_data[size.lower()]
if add_peperoni.lower() == 'y':
    summary += pizza_data['pepperoni'][size.lower()]
summary += pizza_data['extra_cheese'][extra_cheese.lower()]

print(f"Your final bill is: {round(summary, 2)}")
