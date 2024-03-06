import random

import random

min = input("Enter the minimum number between 1 and 1000: ")
max = input("Enter the maximum number between 1 to 1000: ")
quantity = input("Enter the number of numbers in the winning combination: ")

def get_numbers_ticket(min, max, quantity):
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
        if min < 1 or max > 1000 or min>=max or quantity < 1 or quantity > (max - min + 1):
          print("Invalid parameters.")
          return []
        return sorted(random.sample(list(range( min, max + 1)), quantity))
    except Exception:
        print("Please enter whole numbers")
        exit()
print("Winning numbers", get_numbers_ticket(min, max, quantity))
