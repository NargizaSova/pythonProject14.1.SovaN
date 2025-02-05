from src.main import Product, Category
from typing import List


# Тесты для класса Product
def test_product_initialization():
    product = Product("Laptop", "High-end laptop", 1200.99, 10)

    assert product.name == "Laptop"
    assert product.description == "High-end laptop"
    assert product.price == 1200.99
    assert product.quantity == 10


# Тесты для класса Category
def test_category_initialization():
    category = Category("Electronics", "Various electronic devices")

    assert category.name == "Electronics"
    assert category.description == "Various electronic devices"
    assert isinstance(category.products, List)  # Убедимся, что products — это список


def test_category_product_count():
    category = Category("Electronics", "Various electronic devices")
    assert Category.total_products == 0  # На момент создания категории товаров в ней нет

    # Создадим товары
    product1 = Product("Laptop", "High-end laptop", 1200.99, 10)
    product2 = Product("Phone", "Smartphone with great features", 800.50, 15)

    # Добавим товары в категорию
    category.add_product(product1)
    category.add_product(product2)

    assert Category.total_products == 2

def test_category_count():
    assert Category.total_categories == 0

    # Создаем категории
    category1 = Category("Electronics", "Various electronic devices")
    category2 = Category("Home Appliances", "Appliances for home")

    assert Category.total_categories == 2


def test_product_in_category():
    category = Category("Electronics", "Various electronic devices")
    product1 = Product("Laptop", "High-end laptop", 1200.99, 10)

    # Добавим продукт в категорию
    category.add_product(product1)

    # Проверим, что продукт добавлен в список продуктов категории
    assert len(category.products) == 1
    assert category.products[0] == product1