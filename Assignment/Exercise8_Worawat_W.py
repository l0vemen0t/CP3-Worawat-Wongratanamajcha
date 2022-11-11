usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "Wong" and passwordInput == "4321":
    print("Welcome!")
    print("---- Wong Coffee ----")
    print("We always serve with ice!")
    print("1. Special Menu drink! = 80 Bath")
    print("2. Americano           = 55 Bath")
    print("3. Vanilla Latte       = 70 Bath")
    print("4. Matcha              = 65 Bath")
    print("5. Thai tea            = 60 Bath")
    userSelected = int(input(">>"))
    if userSelected == 1:
        total = int(input("How many cup would you like? "))
        print(total*80)
    elif userSelected == 2:
        total = int(input("How many cup would you like? "))
        print(total*55)
    elif userSelected == 3:
        total = int(input("How many cup would you like? "))
        print(total*70)
    elif userSelected == 4:
        total = int(input("How many cup would you like? "))
        print(total*65)
    elif userSelected == 5:
        total = int(input("How many cup would you like? "))
        print(total*60)
    else:
        print("Sorry we don't have other Menu, please come agian!!")
