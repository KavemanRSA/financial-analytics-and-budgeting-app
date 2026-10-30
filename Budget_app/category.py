"""Budget category and ledger operations."""


class Category:
    """A budget category that tracks deposits, withdrawals, and transfers."""

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Record a deposit in the category ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Record a withdrawal if the category has enough funds."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Return the current category balance."""
        return sum(record["amount"] for record in self.ledger)

    def transfer(self, amount, category):
        """Transfer funds to another category if enough funds are available."""
        if category is self:
            return False

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Return whether the requested amount is available."""
        return amount <= self.get_balance()

    def __str__(self):
        width = 30
        left_padding = (width - len(self.name)) // 2
        right_padding = width - len(self.name) - left_padding
        header = f"{'*' * left_padding}{self.name}{'*' * right_padding}"

        ledger_items = "\n".join(
            f"{record['description'][:23]:<23}{record['amount']:>7.2f}"
            for record in self.ledger
        )
        total = f"Total: {self.get_balance():.2f}"
        return f"{header}\n{ledger_items}\n{total}"
