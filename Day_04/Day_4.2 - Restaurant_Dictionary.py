# Restaurant Menu with Lists and Dictionaries

# ----- Simple Lists -----
menu = ['dal', 'paneer', 'noodles']
price = [100, 350, 300]

print("Simple Menu using Lists")
print(menu[0], ':', price[0])  # Outputs: dal : 100

# ----- Dictionary Example -----
restaurant_menu = {
    'dal': 100,
    'paneer': 300,
    'noodles': 350
}

print("\nMenu using Dictionary")
print(restaurant_menu, type(restaurant_menu), id(restaurant_menu))

# ----- Nested Dictionary Example -----
restaurant = {
    'name': 'Kylin Experience',
    'description': 'Asian, Chinese, Sushi, Thai, Sichuan, Beverages',
    'address': '312 A, 3rd Floor, Elante Mall, Phase 1, Chandigarh Industrial Area, Chandigarh',
    'operating_hours': '11am to 11:30pm',
    'price_for_two': 1900,
    'phone': '+919501654007',
    'menu': [
        {
            'name': 'Exotic Vegetables Bowl',
            'price': 750,
            'description': 'A vibrant mix of exotic vegetables is stir-fried'
        },
        {
            'name': 'Veg Khow Suey Bowl',
            'price': 650,
            'description': 'Creamy coconut curry poured over noodles with veggies'
        }
    ]
}

print("\nDetailed Restaurant Info")
print("Name:", restaurant['name'])
print("Operating Hours:", restaurant['operating_hours'])
print("First Menu Item:", restaurant['menu'][0])
