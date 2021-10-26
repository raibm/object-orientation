def create(cod, name, limit, balance, ):
    account = {"cod": cod, "name": name, "limit": limit, "balance": balance}
    return account


def add_credit(account, value):
    account["balance"] += value
    return account


def subtract_credit(account, value):
    account["balance"] -= value
    return account


def get_balance(account):
    return account["balance"]
