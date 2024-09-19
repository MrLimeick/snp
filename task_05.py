from datetime import date, timedelta

def date_in_future(num):
    date1 = date.today()
    if(isinstance(num, int)): date1 += timedelta(days=num)
    return date1

date_in_future([]) # => текущая дата
date_in_future(2)  # => текущая дата + 2 дня