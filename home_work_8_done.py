from datetime import datetime, timedelta

Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday= [], [], [], [], [], [], []

week_days = {0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday, 
             4: Friday, 5: Saturday, 6: Sunday}

TODAY = datetime.now().date()


def get_birthdays_per_week(date):
    new_date = []

    for employee in date:
        employees_birthday_new = datetime(TODAY.year, 
                                      month=employee.get('birthday').month, 
                                      day=employee.get('birthday').day).date()

        employee['birthday'] = employees_birthday_new
        new_date.append(employee)
        
    return difference_today_and_birthday(new_date)


def difference_today_and_birthday(new_date):  

    for employee in new_date:

        diff = employee.get('birthday') - TODAY

        if 0 <= diff.days < 7:
            day_of_week = employee.get('birthday').weekday() 
            week_days.get(day_of_week).append(employee.get('name'))
        
        elif diff.days < -358: #Якщо поточна дата в кінці грудня, а дн на початку наст.року
            
            day_of_week = (employee.get('birthday') + timedelta(days=365)).weekday()
            week_days.get(day_of_week).append(employee.get('name'))

        Mon, Tue, Wed, Thr, Fri, Sat, Sun = ', '.join(Monday), ', '.join(Tuesday),\
                                            ', '.join(Wednesday), ', '.join(Thursday),\
                                            ', '.join(Friday), ', '.join(Saturday), \
                                            ', '.join(Sunday)

    if Mon:
        print(f'Monday: {Mon}, {Sat}, {Sun} ')
    if Tue:
        print(f'Tuesday: {Tue}')
    if Wed:
        print(f'Wednesday: {Wed}')
    if Thr:
        print(f'Thursday: {Thr}')
    if Fri:
        print(f'Friday: {Fri}')
    
# print(get_birthdays_per_week([{'name' : 'Tim', 
#                                'birthday' : datetime(year=2000, month=8, day=4)},
#                               {'name' : 'Sam' , 
#                                'birthday' : datetime(year=1998, month=7, day=31)}, 
#                               {'name' : 'Ann', 
#                                 'birthday' : datetime(year=2002, month=8, day=1)}, 
#                               {'name' : 'Jeane', 
#                                'birthday' : datetime(year=1989, month=8, day=6)},
#                               {'name' : 'Annie', 
#                                 'birthday' : datetime(year=2005, month=8, day=3)},
#                               {'name' : 'Ben', 
#                                 'birthday' : datetime(year=2002, month=8, day=2)},
#                               {'name' : 'Bobi', 
#                                 'birthday' : datetime(year=2012, month=5, day=2)},
#                               {'name' : 'Tim', 
#                                'birthday' : datetime(year=2000, month=1, day=2)},
#                               {'name' : 'Sam' , 
#                                'birthday' : datetime(year=1998, month=1, day=1)}, 
#                               {'name' : 'Ann', 
#                                 'birthday' : datetime(year=2002, month=8, day=1)}, 
#                               {'name' : 'Jeane', 
#                                'birthday' : datetime(year=1989, month=8, day=6)},
#                               {'name' : 'Annie', 
#                                 'birthday' : datetime(year=2005, month=12, day=31)},
#                               {'name' : 'Ben', 
#                                 'birthday' : datetime(year=2002, month=12, day=29)},
#                               {'name' : 'Bobi', 
#                                 'birthday' : datetime(year=2012, month=12, day=30)}
#                                 ]))
                            