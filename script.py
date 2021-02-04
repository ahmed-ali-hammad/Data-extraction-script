from datetime import date, timedelta, datetime
import pandas as pd
import os, re, glob

path = r'\MainFolder\Subfolder1\Subfolder2\Subfolder3\SearchFolder\*.csv' #the directory path


list_of_files = glob.glob(path) #this gets the a list of the .csv files in the given directory


keyword = 'Cash Activities' #the keyword to search with

#the list of dates to search with
dates = []
d1 = date(2020, 10, 1)  #start date
d2 = date(2020, 12, 31)  #end date


for i in range((d2-d1).days + 1):
    d = d1 + timedelta(days=i) #date range
    dates.append(datetime.strptime(str(d), '%Y-%m-%d').strftime('%Y%m%d'))


desired_date = []

#looping through the entire list of files
for fname in list_of_files:
	if keyword in fname:
		for date in dates:
			if date in fname: 
				df = pd.read_csv(fname)
				desired_date.append(df)
			else:
				pass
	else:
		pass

frame = pd.concat(desired_date, axis=0, ignore_index=True)
frame.to_excel (r'\MainFolder\Subfolder1\Subfolder2\Subfolder3\SearchFolder\main.xlsx', "a", index = None, header=False)

#to launch the excel file
os.system('start "excel" "\\MainFolder\\Subfolder1\\Subfolder2\\Subfolder3\\SearchFolder\\main.xlsx"')