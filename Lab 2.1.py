def search(products, product):
    try: return products.index(product)
    except ValueError: return None

product_names = [
    "USB Flash Drive",
    "Speaker",
    "Webcam",
    "Webcam",
    "Microphone",
    "Projector",
    "Laptop",
    "Microphone",
    "Drone",
    "USB Flash Drive"
]
print(search(product_names, 'Drone'))
