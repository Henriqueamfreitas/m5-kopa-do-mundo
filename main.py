# from .menu import products
from management.product_handler import get_product_by_id, get_products_by_type, add_product, \
                                       products, menu_report
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    try:
        print('get_product_by_id:', get_product_by_id('25'))
    except TypeError as e:
        print(e)

    try:
        print('get_products_by_type:', get_products_by_type(1))
    except TypeError as e:
        print(e)

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print('add_product1:', add_product(products, **new_product))
    print('add_product:2', add_product([], **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    print('calculate_tab:', 'table1:', calculate_tab(table_1), 'table2:', calculate_tab(table_2))
    print('menu_report:', menu_report())

