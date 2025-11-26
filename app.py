import json;
DATA_FILE = "data.json"

def load_expenses():
  with open(DATA_FILE,"r") as f:
    return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

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
  save_expenses(expenses)
  print("Expenses Added successfully")

def view_expense():
    data = load_expenses()   # always safe
    if not data:
        print("No expenses found.")
        return
    print("\n===== All Expenses =====")
    for item in data:
        print(f"{item['title']} -- {item['amount']} -- {item['category']}")

def delete_expense():
  
  data = load_expenses()
  if not data:
    print("No Expenses found.")
    return
    # show list to user
  print("\n===== Expenses =====")
  for i, item in enumerate(data, start=1):
        print(f"{i}. {item['title']} -- {item['amount']} -- {item['category']}")
  index = input("Please Enter index to delete")
  if not index.isdigit():
        print("Invalid input. Please enter a number.")
        return

  index = int(index)
  if (1 <= index) and (index <= len(data)):
    del data[index-1]
    print("Data Deleted Successfully")
    save_expenses(data)
    
  else:
    print("index does not exist")

def show_total():
  data = load_expenses() 
  total_expense = 0
  if not data:
        print("No expenses found.")
        return
  
  total_expense = sum(item['amount'] for item in data)
  print(f"Total Amount -- {total_expense}")

def search_expense():
  data = load_expenses()
  if not data:
        print("No expenses found.")
        return
  term = input("Enter the search term").strip().lower()
  results = []
  for i, item in enumerate(data, start=1):
    if term in item['title'].lower():
      results.append((i,item))
  if not results:
     print("No expenses match your search.")
     return
  print("\n===== Search Results =====")
  for i, item in results:
        print(f"{i}. {item['title']} -- {item['amount']} -- {item['category']}")

def search_by_category():
   data = load_expenses()
   if not data:
      print("No Expenses Found")
      return
   term = input("Enter Category to filter(Food, trave, Shopping, Other)").strip().lower()
   
   results = []
   for i,item in enumerate(data, start=1):
      if term in item['category'].lower():
        results.append((i,item))
   if not results:
    print("No expenses match your category")
    return
   print("\n==== Search Results ====")
   for i, item in results:
      print(f"{i}.{item['title']} -- {item['amount']} -- {item['category']}")

def show_menu():
  print("\n============== Expense Manager===============")
  print("1. Add Expense")
  print("2. View All Expense")
  print("3. Delete Expense")
  print("4. Total Expense")
  print("5. Search Expense")
  print("6. Search By Category")
  print("7. Exit")

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
      search_expense()
    elif choice == "6":
      search_by_category()
    elif choice == "7":
      print("Good Bye!")
      break;
    else:
      print("Invalid Choice. Try again");




if __name__ == "__main__":
    main()
