from main1 import logger


@logger
def open_cook_book(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        cook_book = {}
        for dish_name in file:
            ingredient_count = int(file.readline())
            ingredient_list = []
            for i in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredient_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish_name.strip()] = ingredient_list
    return cook_book


# print('Кулинарная книга:')
# print(json.dumps(cook_book, ensure_ascii=False, indent=3))


@logger
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_dict = {}
    ingr_list = []
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                dublicate_ingr = int(ingr['quantity'])
                if ingr['ingredient_name'] not in ingr_list:
                    ingr_dict = {'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count}
                else:
                    ingr_dict = {'measure': ingr['measure'],
                                 'quantity': (int(ingr['quantity']) + dublicate_ingr) * person_count}
                shop_dict[ingr['ingredient_name']] = ingr_dict
                ingr_list.append(ingr['ingredient_name'])
        else:
            print('Ошибка в названии блюд!')
    # print('Купить в магазине для блюд:', dishes[0], ',', dishes[1], ' на ', person_count, ' персон:')
    # print(json.dumps(shop_dict, ensure_ascii=False, indent=3))
    return shop_dict


if __name__ == '__main__':
    cook_book = open_cook_book('cook_book.txt')
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
