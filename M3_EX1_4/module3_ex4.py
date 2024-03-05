from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if birthday < today: # If birthday is in the past
            birthday = birthday.replace(year=today.year + 1)    
            days_to_birthday = (birthday - today).days
            

        if birthday.weekday() >= 5:  # If birthday is on Saturday or Sunday
            birthday = birthday + timedelta(days=7 - birthday.weekday())

        elif days_to_birthday <= 7:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d")})
    return upcoming_birthdays
users = [
    {"name": "John Smith", "birthday": "2000.03.17"},
    {"name": "Mary Elison", "birthday": "2001.03.08"},
    {"name": "Bob Barry", "birthday": "1999.03.01"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Upcoming Birthdays:", upcoming_birthdays)