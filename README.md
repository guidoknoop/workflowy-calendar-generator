# workflowy-calendar-generator
Generate a custom calendar for your WorkFlowy setup

You can use this code to generate a WorkFlowy calendar for one year, that will copy to your clipboard. You can paste it at any location in WorkFlowy with CTRL + V.

The used modules are standard libraries of Python. You can change the variables under the Settings comment.

## Preview
![image](https://user-images.githubusercontent.com/29152658/204143885-89a0c417-7244-49c4-86f6-3a4f4398b2da.png)

## Code
```python
import calendar
import clipboard
from datetime import timedelta, date
import locale

# Settings
LOCALE = 'nl_NL'            # Which locale would you like to use? Choose from https://www.localeplanet.com/icu/
year = 2023                 # For which year would you like to generate a calendar?
display_date = '%d-%m-%Y'   # How would you like to display the date? Choose from https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
display_week = True         # Set to True if you want to see the number of the week as a tag, False if not

# Don't change anything after this line
locale.setlocale(locale.LC_ALL, LOCALE)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(year, 1, 1)
end_date = date(year + 1, 1, 1)

html = f'<?xml version="1.0"?><opml version="2.0"><body><outline text="{year}">'

for single_date in daterange(start_date, end_date):
    if single_date.day == 1:
        html += f'<outline text="{single_date.strftime("%B").upper()}">'

    if not display_week:
        html += f'<outline text="{single_date.strftime(display_date)}" _note="{single_date.strftime("%a")}" />'
    else:
        html += f'<outline text="{single_date.strftime(display_date)}" _note="{single_date.strftime("%a")} | #wk{single_date.strftime("%W")}-{single_date.strftime("%y")}" />'

    day = single_date.day
    month = single_date.month
    year = single_date.year

    if day == calendar.monthrange(year, month)[1]:
        html += '</outline>'

html += '</outline></body></opml>'

clipboard.copy(html)
```
