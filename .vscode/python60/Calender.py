# program to display calender of the given month and year

# importing calender module
import calendar

yy = 2021 # year
mm = 4    # month

# to take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calender
print(calendar.month(yy, mm))
