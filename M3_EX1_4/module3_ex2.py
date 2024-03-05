import random

def get_numbers_tickets(min, max, quantity):
  numbers = set()
  while len(numbers) < quantity:
    numbers.add(random.randint(min, max))
  return sorted(list(numbers))

min = 1  
max = 49
quantity = 6
numbers = get_numbers_tickets(min, max, quantity)
print(f'Your lottery numbers are: {numbers}')

