from datetime import datetime, timedelta
users = [
    {"name": "John Doe", 'birthday': "1985.01.27"},
    {"name": "Emily Way", 'birthday': "1990.01.16"},
    {"name": "Richard Esom", 'birthday': "1990.03.15"},
    {"name": "David Jackson", 'birthday': "1990.03.16"},
    {"name": "Jane Smith", 'birthday': "1990.03.10"},
]
def find_next_weekday(d, weekday: int):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)
def prepare_users(users):
    prepared_list = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            prepared_list.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            print(f'Некоректна дата народження для користувача {user['name']}: {e}')
    return prepared_list
def get_upcoming_birthdays(prepared_list, days=7):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in prepared_list:
        birthday_this_year = user['birthday'].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return upcoming_birthdays

prepared_list = prepare_users(users)
print(get_upcoming_birthdays(prepared_list))
          
