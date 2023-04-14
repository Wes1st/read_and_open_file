import os
from pprint import pprint


def get_cook_books():
    current = os.getcwd()
    folder = 'cook_book'
    file_name = 'recipes.txt'
    full_path = os.path.join(current, folder, file_name)

    with open(full_path, 'rt', encoding='utf-8') as file:
        cook_book = {}

        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline())
            ingredient = []

            for val in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredient.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish_name] = ingredient

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for ingredient in get_cook_books()[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] = \
                    int(shop_list[ingredient['ingredient_name']]['quantity']) \
                    + int(ingredient['quantity'])
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity']}
    for ingredient in shop_list:
        for quantity in shop_list[ingredient]:
            if quantity.__eq__('quantity'):
                shop_list[ingredient][quantity] = \
                    int(shop_list[ingredient][quantity]) * person_count
    return shop_list


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
