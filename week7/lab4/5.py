items = {
    "Pen": 20,
    "Book": 100,
    "Pencil": 10,
    "Bag": 500
}

result = sorted(items.items(), key=lambda x: x[1])

for item, price in result:
    print(item, ":", price)