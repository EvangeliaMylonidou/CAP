import datetime
import pandas as pd

print(pd.date_range(start='1/1/2018', end='1/08/2018'))
dt1 = datetime.datetime.strptime('07:31:50', '%H:%M:%S')
dt2 = datetime.datetime.strptime('20:42:12', '%H:%M:%S')
dt3 = datetime.datetime.strptime('20:42:12', '%H:%M:%S').time()

new = datetime.datetime(hour=8, minute=10, second=10, microsecond=999)
new2 = datetime.datetime(hour=22, minute=0, second=0, microsecond=000)

print(dt1)
print(dt2)
print(dt3)
print()
print(dt2 - dt1)

print(new)
print(new2)
print()
print(new - new2)
