# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''The script allows users to select a month and have the
monthly average temperature at the Helsinki Malmi airport printed to the screen.
Description:
    This script is only a test for a planned version that would read monthly
    average temperatures for the specific observation station from a file and 
    allow users to get the monthly average temperature of any months. 
    Currently, the user should specify the desired month at the start of the
    script as input and the monthly average temperature is written to the screen
    as output.
Limitations:
    This code will not work if the month is not in list of month names.
Usage:
    ./average_temps.py
Author:
    Pavel Zhuchkov - 17.03.2018
Modified by:
    None
'''

# Create and fill lists of months and monthly average temperatures
months = ['January','February','March','April','May','June','July','August',\
                  'September','October','November','December']
monthlyaveragetemperatures = [-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, \
                              11.5, 6.0, 2.0, -1.5]
# Set the selected month
selectedMonth = 'March'

# Find location of the selected month
monthIndex = months.index(selectedMonth)

# Find value of monthly average temperature of the selected month
monthlyaveragetemperature = monthlyaveragetemperatures[monthIndex]

# Print monthly average temperature of the selected month
print('The average temperature in Helsinki in', selectedMonth, 'is', \
      monthlyaveragetemperature)