import calendar
import clipboard
from datetime import timedelta, date
import locale

# Settings
LOCALE = 'en_EN'            # Which locale would you like to use? Choose from https://www.localeplanet.com/icu/
year = 2024                 # For which year would you like to generate a calendar?
display_date = '%m-%d-%Y'   # How would you like to display the date? Choose from https://docs.python.org/3/library/datetime.opml#strftime-and-strptime-format-codes
display_week = True         # Set to True if you want to see the number of the week as a tag, False if not.

# Don't change anything after this line
locale.setlocale(locale.LC_ALL, LOCALE)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(year, 1, 1)
end_date = date(year + 1, 1, 1)

opml = f'<?xml version="1.0"?><opml version="2.0"><body><outline text="{year}">'

for single_date in daterange(start_date, end_date):
    if single_date.day == 1:
        opml += f'<outline text="{single_date.strftime("%B").upper()}">'

    if not display_week:
        opml += f'<outline text="{single_date.strftime(display_date)}" _note="{single_date.strftime("%a")}" />'
    else:
        opml += f'<outline text="&lt;time startYear=&quot;{single_date.year}&quot; startMonth=&quot;{single_date.month}&quot; startDay=&quot;{single_date.day}&quot;&gt;{single_date.strftime(display_date)}&lt;/time&gt; " _note="{single_date.strftime("%a")} | #wk{single_date.strftime("%W")}-{single_date.strftime("%y")}" />'
    day = single_date.day
    month = single_date.month
    year = single_date.year

    if day == calendar.monthrange(year, month)[1]:
        opml += '</outline>'

opml += '</outline></body></opml>'

clipboard.copy(opml)
