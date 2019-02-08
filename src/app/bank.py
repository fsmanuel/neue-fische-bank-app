import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        assert isinstance(account, app.Account), 'Account should be an app.Account'
        assert not self._account_exists(account), f'Account number {account.number} already taken!'

        self.accounts[account.number] = account
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert isinstance(sender, app.Account), 'Sender should be an app.Account'
        assert isinstance(recipient, app.Account), 'Recipient should be an app.Account'

        assert self._account_exists(sender), 'Sender has no account yet!'
        assert self._account_exists(recipient), 'Recipient has no account yet!'

        transaction = app.Transaction(sender=sender.number,
                                      recipient=recipient.number,
                                      subject=subject,
                                      amount=amount)

        sender.subtract_from_balance(amount)
        recipient.add_to_balance(amount)

        self.transactions.append(transaction)
        return transaction

    def _account_exists(self, account):
        return account.number in self.accounts
