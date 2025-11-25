import json;
DATA_FILE = "data.json"

def load_expenses():
  with open(DATA_FILE,"r") as f:
    return json.load(f)

def save_expenses(expense):
  with open (DATA_FILE,"w") as f:
    json.dump(expense, f, indent=4)

def add_expense():

  expenses = load_expenses()

  title = input("Add Expense Title")
  amount = input("Enter Amount")

  try:
    amount = float(amount)
  
  except ValueError:
    print("Amount must be a number")
    return
  
  category = input("Enter Category (Food, Travel, Shopping, Other)")

  expense = {
    "title": title,
    "amount": amount,
    "category": category 
  }

  expenses.append(expense)
  save_expenses(expense)
  print("Expenses Added successfully")

def view_expense():
  with open(DATA_FILE,"r") as f:
     data = f.read()
    #  print(f"{data.title}--{data.amount}")

def show_menu():
  print("\n============== Expense Manager===============")
  print("1. Add Expense")
  print("2. View All Expense")
  print("3. Delete Expense")
  print("4. Total Expense")
  print("5. Exit")

def main():
  while True:
    show_menu()
    choice = input("Enter Choice: ")
    if choice == "1":
      add_expense()
    elif choice == "2":
      view_expense()
    elif choice == "3":
      delete_expense()
    elif choice == "4":
      show_total()
    elif choice == "5":
      print("Good Bye!")
      break;
    else:
      print("Invalid Choice. Try again");




if __name__ == "__main__":
    main()
