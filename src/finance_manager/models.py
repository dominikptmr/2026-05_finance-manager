class Transaction:    
    id_counter = 0

    def __init__(self, date='', amount=0, description='', merchant=''):
        self._date = date # transaction date
        self._amount = amount # transaction amount in EUR
        self._description = description # trasaction description
        self._merchant = merchant # transaction merchant
        self._cathegories = [] # list of cathegories that are applied to the transaction

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
    
    def apply_cathegory(self, cathegory):
        if cathegory not in self.cathegories:
            self.cathegories.append(cathegory)
        else:
            print('Could not add cathegory: Cathegory is already applied to transaction')
    
    def remove_cathegory(self, cathegory):
        if cathegory in self.cathegories:
            self.cathegories.remove(cathegory)
        else:
            print('Could not remove cathegory: Cathegory is not applied to transaction')
    
    def get_id(self):
        return self._id
    
    def is_earning(self):
        return self.amount >= 0
    
    def is_spending(self):
        return self.amount < 0


class Cathegory:
    def __init__(self, name):
        self.name = name


class CathegorizationRule:
    def __init__(self, target, value, cathegory):       
        self.target = target # database column the rule targets (description or merchant)
        self.value = value # value the target item needs to contain, in oder for the rule to apply
        self.cathegory = cathegory # cathegory that is applied to the transaction if the rule applies