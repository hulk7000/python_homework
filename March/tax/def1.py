from price_dict import data_source,food_dic

def count_price(item, amount):
    price = data_source.get(item)

    if price is None:
        return "Item not found"

    result = price * amount
    return f"The price for the items is ${result}"

print(count_price("eggs", 5))

def total_with_tax(subtotal):
    tax = subtotal * 0.08
    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": subtotal + tax
    }

# print(total_with_tax(20))

def delivery_price(item, amount):
    price = food_dic.get(item)

    if price is None:
        return "Invalid item"

    subtotal = price * amount

    if subtotal < 30:
        return f"The total costs ${subtotal + 6}"
    else:
        return f"The total costs ${subtotal}"

print(delivery_price("burger", 1))