class Category:

    # amount
    # category

    # create attibutes
    # amount = 0

    # def __init__(self):
    #     self.categoty = ["Food", "Clothing", "Entertainment"]

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "Successful deposit of {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "Current amount: {}".format(self.amount)

    def check_balance(self, amount):
        # return a boolean, checks if amount is less or greater than self.amount
        if amount > self.amount:
            return True
        else:
            return False

    def withdrawal(self, amount):
        self.amount -= amount
        return "Successful withdrawal of {} in {} category".format(amount, self.category)

    def transfer(self, amount,category):
        # transfer between two instantiated categories
        #self.amount += amount
        #self.amount -= amount        

        return self.withdrawal(amount) + " to " + category.deposit(amount)


# print(v.deposit())

food_category = Category("food", 500)
clothing_category = Category("clothing", 200)
car_category = Category("car", 2000)
vacation_category = Category("vacation", 1000)


print(food_category.deposit(100))

print(food_category.budget_balance())

print(clothing_category.check_balance(50))

print(vacation_category.withdrawal(500))

print(vacation_category.transfer(50, car_category))
