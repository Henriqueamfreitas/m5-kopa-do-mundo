# from ..menu import products
from management.product_handler import products

def calculate_tab(list):
    total_tab = 0
    for item in list:
        amount = item['amount']
        id = item['_id']
        price = 0
        for product in products:
            if(product['_id'] == id):
                price = price + product['price']
        total_product_price = price*amount
        total_tab = total_tab + total_product_price
        formated_total_tab = f"${total_tab:.2f}"
    if formated_total_tab[-1] == '0': 
        return {'subtotal': formated_total_tab[:-1]}
    else:
        return {'subtotal': formated_total_tab}

