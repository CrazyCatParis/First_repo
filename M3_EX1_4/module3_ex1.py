from datetime import datetime
def date(input_date: str):
    while True:
        try:
            input_datetime = datetime.strptime(input_date, "%Y-%m-%d")
        except ValueError:
            return None
        return input_datetime

def get_days_from_today(input_date: str):
    input_datetime_paramenter = date(input_date)
   
    if not input_datetime_paramenter:
        return []
    today = datetime.today()
    difference = (input_datetime_paramenter - today).days
    print(f'Your date is {difference} days from today')
    return difference


if __name__ == "__main__":

      input_date = input('Please enter date in format YYYY-MM-DD: ')
      print(get_days_from_today(input_date))
