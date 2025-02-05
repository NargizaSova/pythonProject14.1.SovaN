import pytest
from src.main import Product, Category



@pytest.fixture
def sample_product():
    """Фикстура для создания объекта Product"""
    return Product("Laptop", "High-end laptop", 1200.99, 10)

@pytest.fixture
def another_product():
    """Еще один продукт для проверки работы с категориями"""
    return Product("Phone", "Smartphone with great features", 800.50, 15)

@pytest.fixture
def empty_category():
    """Фикстура для создания пустой категории"""
    return Category("Electronics", "Various electronic devices")

@pytest.fixture
def category_with_products(sample_product, another_product):
    """Фикстура для категории, в которую добавлены два товара"""
    category = Category("Electronics", "Various electronic devices")
    category.add_product(sample_product)
    category.add_product(another_product)
    return category