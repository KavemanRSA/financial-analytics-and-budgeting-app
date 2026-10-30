"""Entry point for the budget app."""

from .category import Category
from .reports import create_spend_chart


def main():
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")

    clothing = Category("Clothing")
    clothing.deposit(1000, "initial deposit")
    clothing.withdraw(45.64, "shoes")
    clothing.withdraw(89.15, "clothes and more shoes for the wedding")
    clothing.transfer(50, food)

    print(food)
    print(clothing)
    print(create_spend_chart([food, clothing]))


if __name__ == "__main__":
    main()
