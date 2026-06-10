#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self._last_transaction = None  # (title, price, quantity)

    def add_item(self, title, price, quantity=1):
        self._last_transaction = (title, price, quantity)

        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (100 - self.discount) / 100

        # IMPORTANT: format must match test EXACTLY ($800 not $800.0)
        formatted_total = self._format_total(self.total)

        print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        if not self._last_transaction:
            return

        title, price, quantity = self._last_transaction

        self.total -= price * quantity

        for _ in range(quantity):
            self.items.remove(title)

        self._last_transaction = None

    def _format_total(self, value):
        # Ensures 800.0 -> "800", 800.50 -> "800.5", etc.
        if value == int(value):
            return str(int(value))
        return str(value)
