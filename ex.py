class Expence:

    def __init__(self,name,amount,category):
        self.name = name
        self.amount= amount
        self.category = category

    defm __repr__(self):
        return f"Expense :{self.name} {self.category} {self.amount:.2f}"
