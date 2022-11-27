import calendar
import clipboard
from datetime import timedelta, date
import locale

# Settings
LOCALE = 'nl_NL'    # Which locale would you like to use? Choose from https://www.localeplanet.com/icu/
year = 2023         # For which year would you like to generate a calendar?

# Don't change anything after this line
locale.setlocale(locale.LC_ALL, LOCALE)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(year, 1, 1)
end_date = date(year, 12, 31)

msg = f'<?xml version="1.0"?><opml version="2.0"><body><outline text="{year}">'

for single_date in daterange(start_date, end_date):
    if single_date.day == 1:
        msg += f'<outline text="{single_date.strftime("%B").upper()}">'

    msg += f'<outline text="{single_date.strftime("%d-%m-%Y")}" _note="{single_date.strftime("%a")}" />'

    day = single_date.day
    month = single_date.month
    year = single_date.year

    if day == calendar.monthrange(year, month)[1]:
        msg += '</outline>'

msg += '</outline></body></opml>'

clipboard.copy(msg)