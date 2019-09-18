# -*- coding: utf-8 -*-

import pytest
from wallet import AccountBalance, InsufficientAmount

@pytest.fixture
def account():
    '''Returns an account instance with a zero balance'''
    return AccountBalance()

@pytest.mark.parametrize('deposit, withdraw, expect', [
    (300, 100, 200),
    (200, 20, 180),
    (150.5, 150.5, 0)
])
def test_transaction(account, deposit, withdraw, expect):
    account.deposit_money_to_account(deposit)
    account.withdraw_money_from_account(withdraw)
    assert account.balance == expect


# ========== Simpliest version ==========
# # Tworzenie konta - stan początkowy
# def test_default_initial_amount():
#     account = AccountBalance()
#     assert account.balance == 0
#
# # Tworzenie konta - + bonus za założenie
# def test_setting_initial_amount():
#     account = AccountBalance(100)
#     assert account.balance == 100
#
# # WPŁATA GOTÓWKI
# def test_deposit_money_to_account():
#     account = AccountBalance(1000)
#     account.deposit_money_to_account(9000)
#     assert account.balance == 10000
#
# # WYPŁATA GOTÓWKI
# def test_withdraw_money_from_account():
#     account = AccountBalance(100)
#     account.withdraw_money_from_account(90)
#     assert account.balance == 10
#
# # PRZELEW OD KOGOŚ
# def test_get_transfer_money():
#     account = AccountBalance(1000)
#     account.get_transfer_money(400)
#     assert account.balance == 1400
#
# # PRZELEW DO KOGOŚ
# def test_send_transfer_money():
#     account = AccountBalance(1000)
#     account.send_transfer_money(1000)
#     assert account.balance == 0

