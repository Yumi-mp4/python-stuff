# kalkulator wieku
import calendar
from datetime import date

rok = 1999
miesiac = 12
dzien = 22

dzisiaj = date.today()

lata = dzisiaj.year - rok
miesiace = dzisiaj.month - miesiac
dni = dzisiaj.day - dzien

if dni < 0:
    poprzedni_miesiac = dzisiaj.month - 1
    poprzedni_rok = dzisiaj.year

    if poprzedni_miesiac == 0:
        poprzedni_miesiac = 12
        poprzedni_rok -= 1
    
    dni += calendar.monthrange(poprzedni_rok, poprzedni_miesiac) [1]
    
if miesiace < 0:
    lata -= 1
    miesiace += 12

print(f"{lata} lat, {miesiace} miesiecy, {dni} dni")