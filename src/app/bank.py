class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        account_number = account['number']
        assert not self._account_exists(account), f'Account number {account_number} already taken!'

        self.accounts.append(account)
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert amount > 0, 'Amount has to be greater than 0'
        assert self._account_exists(sender), 'Sender has no account yet!'
        assert self._account_exists(recipient), 'Recipient has no account yet!'

        transaction = {
            'sender': sender,
            'recipient': recipient,
            'subject': subject,
            'amount': amount
        }
        self.transactions.append(transaction)
        return transaction

    def _account_exists(self, account_to_search):
        matches = list(filter(
            lambda account: account == account_to_search,
            self.accounts))

        return matches and len(matches) == 1

    # Informations about the bank
    def infos(self, *, accounts=True, transactions=True):
        print(f'Bank name: {self.name}')

        if accounts:
            self._account_infos()

        if transactions:
            self._transaction_infos()

    def _account_infos(self):
        number_of_accounts = len(self.accounts)
        print(f'Accounts: {number_of_accounts}')

        for account in self.accounts:
            number = account.get('number', None)
            firstname = account.get('firstname', None)
            lastname = account.get('lastname', None)
            print(f'{number} {firstname} {lastname}')

    def _transaction_infos(self):
        number_of_transactions = len(self.transactions)
        print(f'Transactions: {number_of_transactions}')

        for transaction in self.transactions:
            firstname = transaction['sender']['firstname']
            lastname = transaction['sender']['lastname']
            sender = f'{firstname} {lastname}'

            firstname = transaction['receiver']['firstname']
            lastname = transaction['receiver']['lastname']
            receiver = f'{firstname} {lastname}'

            subject = transaction['subject']
            amount = transaction['amount']

            print(f'From {sender} to {receiver} - {subject}: {amount} €')
