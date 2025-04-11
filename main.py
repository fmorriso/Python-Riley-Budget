

# Takes user input to sort income and expenses in budget
def get_type():
    while True:
        transaction_type = input("Enter transaction type ([i]ncome or [e]xpense): ")
        if transaction_type[:1].lower() == 'i':
            return 'Income'
        elif transaction_type[:1].lower() == 'e':
            return 'Expenses'
        else:
            print("Enter either 'i' or 'e'.")


# Takes user input for what the name of the transaction is
def get_category():
    transaction_category = input("Enter a transaction category: ")
    return transaction_category.lower()


# Takes user input for amount of transaction and has an exception to ensure input is a number
def get_amount():
    while True:
        try:
            transaction_amount = float(input("Enter a transaction amount: "))
            return transaction_amount
        except ValueError:
            print("Enter a number.")
            continue


def get_balance() -> float:
    # budget_dict[type_key][category_key] = amount
    balance = 0
    for key, value in budget_dict.items():
        if isinstance(value, dict):
            print(f"Type: {key}")
            balance = get_balance()
            print(f"Type: {key}, Value: {value}")
            balance += value
            # print(balance)
            # print_summary(balance)
    return balance


def print_summary(balance):
    print("\n--- Budget Summary ---")
    print("Balance: $" + str(balance))
    for transaction_type, categories in budget_dict.items():
        print(f"\n{transaction_type}:")
        if categories:
            for category, amount in categories.items():
                print(f"  {category.capitalize()}: ${amount:.2f}")
        else:
            print("  No entries.")


# Uses a dictionary and initial values for income/expenses to create budget
#def budget(dictionary):
def display_budget(heading):
    print(heading)
    for top_key, sub_dict in budget_dict.items():
        print(top_key)
        for category, amount_string in sub_dict.items():
            amount = float(amount_string)
            print("\t" + category  + ": " + str(amount))
    print('Total Income: $' + str(total_income))
    print('Total Expenses: $' + str(total_expenses))


###### MAIN LOGIC STARTS HERE ##################
budget_dict = {'Income': {}, 'Expenses': {}}
total_income = 0
total_expenses = 0
while True:
    # Take user input for transaction type, category, and amount, or done to exit
    user_input = input("Hit 'enter' key for transaction or enter 'done' if finished: ")
    if user_input == 'done':
        break
    # Uses above functions to define order of keys/values in the dictionary
    type_key = get_type()
    category_key = get_category()
    amount = get_amount()

    budget_dict[type_key][category_key] = amount

    # Assigns amount of transaction to type based on result of user input
    if type_key == 'Income':
        total_income += amount
    else:
        total_expenses += amount
    print("Income: " + str(total_income) + " Expenses: " + str(total_expenses))


display_budget('Final Budget: ')
    # Iterates through dictionary keys to print itemized income and expenses report
    #print("Final budget: ")
    # for type_key in budget_dict:
    #     print(type_key + ": ")
    #     for category_key in budget_dict[type_key]:
    #         print(category_key + ": " + )

    # print(budget_dict)
    # for type_key in budget_dict:
    #     print(f"{type_key}")
    #     for sub_key, value in budget_dict.items():
    #         for value in value.items():
    #             #print(f"  Sub Key: {sub_key}, Value: {value}")
    #             print(f"  Value: {value}")
    #get_balance(budget_dict)
    #get_balance()


# Creates dictionary for transaction


#budget(budget_dict)

# # Example usage:
# my_dict = {
#     'income': {},
#     'expenses': {}
# }

# balance = print_nested_values(my_dict)
# print("Final Balance:", balance)