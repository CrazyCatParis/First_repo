from datetime import datetime

def input_function():
   while True:
       try:
           input_date = input('Please enter date in format YYYY-MM-DD: ')
           input_datetime = datetime.strptime(input_date, "%Y-%m-%d")
           break
       except ValueError:
           print('Incorrect data format, should be YYYY-MM-DD')
   return input_datetime


def get_days_from_today(input_datetime_paramenter):
    today = datetime.today()
    difference = (input_datetime_paramenter - today).days
    print(f'Your date is {difference} days from today')
    return difference

get_days_from_today(input_function())
