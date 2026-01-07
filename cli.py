from loan import Loan
from repository import LoanRepository
from loanservice import LoanService

repo = LoanRepository()
service = LoanService(repo)

def cli(service: LoanService):

    try:
        print("Main Menu")
        print("-" * 15)
        print("1. Add loan;")
        print("2. Remove loan;")
        print("3. List loans;")
        print("4. Exit program;\n")

        answer = int(input("Number of option: "))
        print("\n\n")
        if answer not in [1, 2, 3, 4]:
            print("Not a valid option number.")
            return True
    except ValueError as e:
        print(f"Error: {e}")
        print("Insert 1, 2, 3 or 4 for their respective actions.\n")
        return True
    
    if answer == 1:
        user = input("Insert user's name: ")
        book = input("Insert book's name: ")
        service.add_loan(user, book)
        print("Loan added successfully.")
        return True

    elif answer == 2:
        user = input("Insert user's name to remove: ")
        book = input("Insert book's name to remove: ")
        try:
            service.remove_loan(user, book)
            print(f"The loan with the user: {user} and book: {book} was removed from the list of loans.\n") 
        except ValueError:
            print("The loan was not found.\n")
        return True
    elif answer == 3:
        loans = service.list_loans()
        for loan in loans:
            print(loan)
            print("-" * 15)
        print("\n")
        return True
    else:
        print("Exiting program.")
        return False

while True:
    if not cli(service):
        break