
from datetime import datetime

today = datetime.today()
future_date = '2027-03-08'

date_string = datetime.strptime(future_date, "%Y-%m-%d")

difference = (date_string - today).days
print(difference)



  
