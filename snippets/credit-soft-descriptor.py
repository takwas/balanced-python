# bank_account_href is the stored href for the BankAccount
# order_href is the stored href for the Order
bank_account = balanced.BankAccount.fetch(bank_account_href)
credit = bank_account.credit(
    amount=100000,
    description='Payout for order #1111',
    appears_on_statement_as='GoodCo #1111',
    order=order_href
)