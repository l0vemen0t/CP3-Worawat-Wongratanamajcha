def vatCal(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
  
price = int(input("Enter Price: "))
print(vatCal(price))
