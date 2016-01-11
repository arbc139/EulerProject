month_dict = {
  1:31,
  2:28,
  3:31,
  4:30,
  5:31,
  6:30,
  7:31,
  8:31,
  9:30,
  10:31,
  11:30,
  12:31
}

def month_date_by_year(month, year):
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_dict[month]


def is_leap(year):
  if year%4 != 0 or (year % 400 != 0 and year % 100 == 0):
    return False
  else:
    return True


answer = list()

year = 1901
month = 1
day = 6 # sunday
month_day_count = month_date_by_year(month, year)

while year < 2001:
  day += 7
  if day > month_day_count:
    day -= month_day_count
    month += 1
    if month > 12:
      month = 1
      year += 1
    month_day_count = month_date_by_year(month, year)

  if day == 1:
    answer.append([year, month, day])

print answer
print len(answer)