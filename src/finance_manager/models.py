
class Transaction:    
    id_counter = 0

    def __init__(self, date='', amount=0, description='', merchant=''):
        self._date = date # transaction date
        self._amount = amount # transaction amount in EUR
        self._description = description # trasaction description
        self._merchant = merchant # transaction merchant
        self._categories = [] # list of categories that are applied to the transaction

        Transaction.id_counter += 1
        self._id = Transaction.id_counter
        
    def __repr__(self):
        return f"Transaction (id={self._id}, amount={self._amount}, merchant='{self._merchant}')"
        
    def set_date(self, date):
        if date and type(date) is str:
            self._date = date
        else:
            raise ValueError('Date could not be set.')
    
    def get_date(self):
        return self._date
    
    def set_amount(self, amount):
        if amount and type(amount) is float:
            self._amount = amount
        else:
            raise ValueError('Amount could not be set')
    
    def get_amount(self):
        return self._amount
    
    def set_description(self, description):
        if description and type(description) is str:
            self._description = description
        else:
            raise ValueError('Description could not be set')
    
    def get_description(self):
        return self._description

    def set_merchant(self, merchant):
        if merchant and type(merchant) is str:
            self._merchant = merchant
        else:
            raise ValueError('Merchant could not be set')
    
    def get_merchant(self):
        return self._merchant
    
    def apply_category(self, category):
        if category not in self._categories:
            self._categories.append(category)
        else:
            print('Could not add category: category is already applied to transaction')
    
    def remove_category(self, category):
        if category in self._categories:
            self._categories.remove(category)
        else:
            print('Could not remove category: category is not applied to transaction')
    
    def get_id(self):
        return self._id
    
    def is_earning(self):
        return self._amount >= 0
    
    def is_spending(self):
        return self._amount < 0
    
    def to_dict(self):
        return {
            "id": self._id,
            "date": self._date,
            "amount": self._amount,
            "description": self._description,
            "merchant": self._merchant,
            "categories": self._categories
        }


class Category:
    def __init__(self, name):
        self.name = name


class CategorizationRule:
    def __init__(self, target, value, category):       
        self.target = target # database column the rule targets (description or merchant)
        self.value = value # value the target item needs to contain, in oder for the rule to apply
        self.category = category # category that is applied to the transaction if the rule applies