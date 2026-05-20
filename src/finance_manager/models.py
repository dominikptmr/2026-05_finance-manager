
class Transaction:    

    def __init__(self, transaction_date='', amount=0, description='', merchant='', id=None):
        self.transaction_date = transaction_date # transaction date
        self.amount = amount # transaction amount in EUR
        self.merchant = merchant # transaction merchant
        self.description = description # trasaction description
        self.id = id
        
    def __repr__(self):
        return f"Transaction: (merchant='{self.merchant}', amount={self.amount})"
    
    def is_earning(self):
        return self.amount >= 0
    
    def is_spending(self):
        return self.amount < 0
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.transaction_date,
            "amount": self.amount,
            "description": self.description,
            "merchant": self.merchant,
        }


class Category:
    def __init__(self, name):
        self.name = name


class CategorizationRule:
    def __init__(self, target, value, category):       
        self.target = target # database column the rule targets (description or merchant)
        self.value = value # value the target item needs to contain, in oder for the rule to apply
        self.category = category # category that is applied to the transaction if the rule applies