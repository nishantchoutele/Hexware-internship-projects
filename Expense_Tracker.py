from ex import Expense



def main():
    print("")
    expense_file_path = "expense.csv"
    budget = 20000
    expense =expense_kitna_hua()




def expence_kitna_hua():
    print("kitna kharcha kiya hai")
    expense_name =input("kharcha kaha kiye ho bolo:")
    expense_amount =float(input("kitne paise yaha pe uddye ho:"))
    print(f"expance name is {expense_name},{expense_amount}")

    expense_categories = ["food","home","work","fun","Misc",]

    while True:
        print("kis category me kharcha kr rahe ho batao: ")
        for i , category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")
        value_range = f"[1-len(expense_categories)]"
        selected_index =(input("bhai category bata do: {value_range}"))-1

        if selected_index in range(len(expence_category)):
            print(selected_category)

            new_expense = Expense(name = expense_name,category = selected_category, amount= expense_amount)
            return new_expense
        else:
            print("invalid category")

        break

def file_me_save_kro(expense_file_path):
    print(f"kharcha file me save krna hai: {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
    



def summerise_expenses(expense_file_path):
    print{"summery of user expenses:"}
    expenses =[]
    with open(expense_file_path,'r') as f:
        f.readlines()
        for line in lines:
            #print(line)
            expense.name,expense.amount,expense.category =line.strip().split(",")
            printI(f"{expense.name},{expense.amount},{expense.category}")
            line_expense = Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            #print(line_expense)
            expenses.append(line_expenses)
            print(expenses)
            
    amount_by_category ={}
    for expense in expenses:
        key=expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("ye aapka category wise kharcha hai")
    for key , amount in amount_by_category.items():
        print(f"{key} : {amount}")

    total_spent = sum[x.amount for x in expenses]
    prinyt(f"itna kharcha kr liye ho  bhai: {total_spent}")

    remaining_budget = budegt - (total_spent)
    print(f"remaining budegt : {remaining_budget:2f}")

    now = datetime.datetime.now()
    days_in_month=calender.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month-now.day
    print("remaining days in this month:", remaining_days)
    if __name__=="__main__"
   main()
