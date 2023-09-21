import _datetime as dt

current = dt.datetime.now()
year = current.year
month = current.month
week_day = current.weekday()

birthday = dt.datetime(year=1989, month=5, day=5)

print(birthday)