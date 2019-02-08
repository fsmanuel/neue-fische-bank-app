class Account:
    def __init__(self, *, firstname, lastname, number, balance=None):
        assert isinstance(number, int), 'Number needs to be an integer'
        if balance is not None:
            assert isinstance(balance, float), 'Balance needs to be a float'

        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance or 0.0

    def info(self):
        template = 'Number {number}: {firstname} {lastname} - {balance} €'
        return template.format(number=self.number,
                               firstname=self.firstname,
                               lastname=self.lastname,
                               balance=self.balance)

    def has_funds_for(self, amount):
        return self.balance >= amount

    def add_to_balance(self, amount):
        assert amount > 0, 'Amount needs to be greater than 0'

        self.balance += amount

    def subtract_from_balance(self, amount):
        assert self.has_funds_for(amount), 'Account has not enough funds'

        self.balance -= amount
