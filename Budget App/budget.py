class Category:

    #constructor 
    def __init__(self, Category, food=" ", clothing=" ", auto=" ", entertainment=" "):
        self.element_category = Category
        self.food = food
        self.clothing = clothing
        self.auto = auto
        self.entertainment = entertainment
        self.ledger = []


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        


    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def check_funds (self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def withdraw (self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    #get initial deposit and return
    def get_deposit (self):
        for item in self.ledger:
            if "deposit" in item["description"]:
                return item["amount"]

            elif "Transfer from" in item["description"]:
                return item["amount"]
            else:
                return None


    #def transfer (self, amount, Category):
    def transfer (self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount, description="Transfer to " + str(Category.element_category))
            Category.deposit(amount, description="Transfer from " + str(self.element_category))
            return True
        else:
            return False 

    #Method that converts budget object to string
    def __str__(self):
        #initial value for the object printout
        ledger_out=""

        #Print title Category (Food)
        ledger_out += '*' * int((30 - len(self.element_category)) / 2) + self.element_category + '*' * int((30 - len(self.element_category)) / 2)

        #loop to iterate ledger
        for item in self.ledger:
            #key/description extraction
            if (len(item["description"]) > 23):
                ledger_out += "\n" + item["description"] [0:23]
            else:
                ledger_out += "\n" + item["description"] + " " * (23 - len(item["description"]))
            
            #value extraction
            ledger_out += " " * (7-len("{:.2f}".format(item["amount"]))) + "{:.2f}".format(item["amount"])
        #return Total
        total = str(self.get_balance())
        ledger_out += "\nTotal: " + total
        #print(total)
        #ledger_out += "\nTotal: " + str(self.get_balance())


        return ledger_out

        
def create_spend_chart(categories):
    #categories = categories
    chart_title = "Percentage spent by category"
    chart_print = chart_title
    horiz_bar = "-" * 10
    horiz_bar = horiz_bar.rjust(14)
    cat_name = []
    vertical_categories = []

    #loop to grab total of each categories
    for i in categories:
        if i.element_category == "Food":
            food_totals = str(i.get_balance())
            food_initial_deposit = i.get_deposit()
            #print(food_initial_deposit)
            continue
        elif i.element_category == "Clothing":
            clothing_totals = str(i.get_balance())
            clothing_initial_deposit = i.get_deposit()
            #print(clothing_initial_deposit)
            continue
        elif i.element_category == "Auto":
            auto_totals = str(i.get_balance())
            auto_initial_deposit = i.get_deposit()
            #print(auto_initial_deposit)
            continue
        elif i.element_category == "Entertainment":
            entertainment_totals = str(i.get_balance())
            entertainment_initial_deposit = i.get_deposit()
            #print(entertainment_initial_deposit)
            continue
        else:
            break
            
    #print(food_totals)
    
    #loop to grab category name
    for i in categories:
        cat_name.append(i.element_category)
    #print(cat_name)

    #produce the categories vertically
    for cat in cat_name:
        vertical_category = ''
        for i in cat:
            vertical_category += i + '\n'
        vertical_categories.append(vertical_category)


    #Get max number of lines/rows
    max_lines = 0
    for vertical_category in vertical_categories:
        num_lines = vertical_category.count('\n')
        if num_lines > max_lines:
            max_lines = num_lines

    #print categories side-by-side
    output = ""
    for i in range(max_lines):
        output += ' ' * 5
        for vertical_category in vertical_categories:
            lines = vertical_category.split('\n')
            if i < len(lines) - 1:
                output += lines[i] + '  '
            else:
                output += '   '
        output += '\n'

    
    #print o's
    food_percent = (food_initial_deposit - float(food_totals)) / food_initial_deposit * 100
    food_percent = int(f'{food_percent:.0f}')
    #print(food_percent)
    clothing_percent = (clothing_initial_deposit - float(clothing_totals)) / clothing_initial_deposit * 100
    clothing_percent = int(f'{clothing_percent:.0f}')
    #print(clothing_percent)
    auto_percent = (auto_initial_deposit - float(auto_totals)) / auto_initial_deposit * 100
    #print(auto_percent)
    #entertainment_percent = (entertainment_initial_deposit - float(entertainment_totals)) / entertainment_initial_deposit * 100
    #print(entertainment_percent)
    percentage_col = ""
    
    print (chart_print)
    for k in range(100, 0, -10):
        percentage = f"{k:3}|"
        if food_percent >= k:
            percentage += " o"

        else:
            percentage += "  "

        if clothing_percent >= k:
            percentage += "  o"

        else:
            percentage += "  "

        if auto_percent >= k:
            percentage += "  o"

        else:
            percentage += "  "

        percentage_col = percentage
        print(percentage_col)
        


    print(horiz_bar + "\n" + output)




