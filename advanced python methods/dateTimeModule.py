import datetime
mytime = datetime.time(2,20)
mytime.minute
mytime.hour
print(mytime)
mytime.microsecond
#se usa 24 horas 
mytime = datetime.time(13,20,1,20)
mytime.minute
mytime.hour
print(mytime)
mytime.microsecond
type(mytime)
#se le puede agregar date object etc, ejemplo:
#today = datetime.date() #year,month, day o:
today = datetime.date.today()
print(today)
today.year
today.month
today.day
today.ctime()#hay que agregarle time information
from datetime import datetime
mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)
mydatetime = mydatetime.replace(year=2020) # reemplaza el de arriba
print(mydatetime)
#arithmetic
#primero solo con date information
from datetime import date 
date1 = date(2021,11,3)
date2 = date(2020,11,3)
resutl = date1 - date2
type(resutl)
#arithmetic date time 
from datetime import datetime
datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
mydiff = datetime1 - datetime2
36000 / 60 / 60
mydiff.seconds #solo los segundos (36000) osea la diferencia entre las horas
mydiff.total_seconds() #toda la diferencia de tiempo en segundos