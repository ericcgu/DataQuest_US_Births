'''
Create a function named dow_births() that takes a single, required argument (a list of lists) and returns a dictionary containing the total number of births for each unique value of the day_of_week column.
Use the dow_births() function to return the day-of-week totals for the dataset and assign the result to cdc_day_births. Display the dictionary.
'''

def readcsv(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        int_fields = []
        rows = infile.read()
        rows_list = rows.split('\n')
        for item in rows_list[1:]:
            int_fields.append(list(map(int,item.split(','))))
        return int_fields

def dow_births(data):
    births_per_day = {}
    for item in cdc_list:
        day = item[3]
        births = item[4]
        if day in births_per_day:
            births_per_day[day] += births
        else:
            births_per_day[day] = births
    return births_per_day

cdc_list = readcsv('data/US_births_1994-2003_CDC_NCHS.csv')
print(dow_births(cdc_list))