import enum


class Coin(enum.IntEnum):
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100


class VendingMachine:

    def __init__(self):
        self.inserted_money = []

    def get_balance(self):
        return sum(self.inserted_money)

    def add_money(self, *coins):
        for coin in coins:
            self.inserted_money.append(coin)

    def return_coins_inserted(self):
        temp = list(self.inserted_money)
        self.inserted_money.clear()
        return temp
