import datetime as dt
from datetime import datetime as dtdt

users = [
  {"name": "John Doe", "birthday": "1985.01.23"},
  {"name": "Jane Smith", "birthday": "1990.01.27"},
  {"name": "Jane Doe", "birthday": "1990.02.18"},

]
birthdayList = []


def get_upcoming_birthdays(users):
    dateNow = dtdt.today().date()
    for user in users:
        birthday = user["birthday"]
        birthday = str(dateNow.year)+birthday[4:]
        birthdayThisYear = dtdt.strptime(birthday, "%Y.%m.%d").date()  
        if birthdayThisYear < dateNow:
           birthdayThisYear = birthdayThisYear.replace(year=birthdayThisYear.year +1) 
           get_birthday_on_week(birthdayThisYear, dateNow, user)
        else :
            get_birthday_on_week(birthdayThisYear, dateNow, user)   
    return birthdayList

def get_birthday_on_week(birthdayThisYear, dateNow, user):
    differenceDays = (birthdayThisYear - dateNow).days
    weekDay = birthdayThisYear.isoweekday()
    if 0<=differenceDays<7  or differenceDays>0:
        if weekDay<6:
           birthdayList.append({"name": user["name"], "birthday": birthdayThisYear.strftime("%Y.%m.%d")})
        else :
            if (birthdayThisYear + dt.timedelta(days=1)).weekday()==0 :
             birthdayList.append({"name": user["name"], "birthday": (birthdayThisYear + dt.timedelta(days=1)).strftime("%Y.%m.%d")}) 
            elif (birthdayThisYear+dt.timedelta(days=2)).weekday()==0:
                    birthdayList.append({'name':user['name'], 'birthday':(birthdayThisYear + dt.timedelta(days=2)).strftime("%Y.%m.%d")})        

print(get_upcoming_birthdays(users))
    
