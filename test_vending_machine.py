import enum

import pytest


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


@pytest.fixture
def machine():
    return VendingMachine()


def test_has_zero_balance_when_powered_on(machine):
    assert machine.get_balance() == 0


def test_can_insert_a_nickel_and_get_balance_returned(machine):
    machine.add_money(Coin.NICKEL)
    assert machine.get_balance() == 5


def test_tracks_value_of_two_nickels(machine):
    machine.add_money(Coin.NICKEL, Coin.NICKEL)
    assert machine.get_balance() == 10


def test_insert_all_values_of_coins(machine):
    machine.add_money(Coin.DIME, Coin.NICKEL, Coin.QUARTER, Coin.DOLLAR)
    assert machine.get_balance() == 140


def test_return_exact_coin_that_inserted(machine):
    machine.add_money(Coin.QUARTER, Coin.QUARTER, Coin.DOLLAR)
    returned_coins = machine.return_coins_inserted()
    assert returned_coins.count(Coin.QUARTER) == 2
    assert returned_coins.count(Coin.DOLLAR) == 1


def test_balance_zero_after_coin_return(machine):
    machine.add_money(Coin.QUARTER, Coin.QUARTER, Coin.DOLLAR)
    machine.return_coins_inserted()
    assert machine.get_balance() == 0


def test_if_no_coins_inserted_return_no_coins(machine):
    returned_coins = machine.return_coins_inserted()
    assert len(returned_coins) == 0
