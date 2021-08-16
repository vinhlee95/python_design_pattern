"""
Problem:

Input: a list of products
Output: a list of products matching particular specifications, e.g. size, color...
"""

# 
# --------- NAIVE IMPLEMENTATION ---------------
# 
from typing import List


class Product:
    name: str
    size: int
    color: str

    def __init__(self, name: str, size: int, color: str) -> None:
        self.name = name
        self.size = size
        self.color = color

    def __repr__(self) -> str:
        return self.name


class ProductFilter:
    @staticmethod
    def filter_by_color(products: List[Product], color: str) -> List[Product]:
        return [product for product in products if product.color == color]

    @staticmethod
    def filter_by_size(products: List[Product], size: int) -> List[Product]:
        return [product for product in products if product.size >= size]


# Test the implementation
iPhone_6 = Product(name="iPhone_6", size=4, color="gray")
iPhone_7 = Product(name="iPhone_7", size=5, color="pink")

product_filter = ProductFilter()
pink_phones = product_filter.filter_by_color(products=[iPhone_6, iPhone_7], color="pink")  # [iPhone 7]
large_phones = product_filter.filter_by_size(products=[iPhone_6, iPhone_7], size=5)


#
# ------------- SPECIFICATION PATTERN ---------------
#
class Specification:
    def is_valid(self, product: Product) -> bool:
        return NotImplemented


class BetterProductFilter:
    def filter_by_specs(self, products: List[Product], specs: List[Specification]):
        return [product for product in products if all(spec.is_valid(product) for spec in specs)]


class ColorSpecification(Specification):
    color: str

    def __init__(self, color: str):
        self.color = color

    def is_valid(self, product: Product) -> bool:
        return product.color == self.color


class SizeSpecification(Specification):
    size: int

    def __init__(self, size: int):
        self.size = size

    def is_valid(self, product: Product) -> bool:
        return product.size == self.size


phone_list = [iPhone_6, iPhone_7]
gray_phones = BetterProductFilter().filter_by_specs(phone_list, specs=[ColorSpecification(color="gray")])
large_phones = BetterProductFilter().filter_by_specs(phone_list, specs=[SizeSpecification(size=5)])


pink_and_large_phones = BetterProductFilter().filter_by_specs(phone_list, specs=[ColorSpecification(color="pink"), SizeSpecification(size=5)])