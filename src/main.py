class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.price = price  # Цена товара
        self.quantity = quantity  # Количество товара в наличии

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Category:
    total_categories = 0  # Атрибут класса: общее количество категорий
    total_products = 0    # Атрибут класса: общее количество товаров

    def __init__(self, name, description):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = []  # Список товаров в категории

        # Обновляем общее количество категорий при создании новой
        Category.total_categories += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            # Обновляем общее количество товаров при добавлении нового продукта
            Category.total_products += 1
        else:
            raise TypeError("Only objects of type Product can be added.")

    def __repr__(self):
        return f"Category(name='{self.name}', products={len(self.products)})"

