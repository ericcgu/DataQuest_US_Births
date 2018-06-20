'''
Create a function named month_births() that:
Takes a single, required argument, a list of lists.
Creates an empty dictionary, births_per_month, to store the monthly totals.
Uses a for loop to:
Iterate over the list of lists,
Extract the value in the month and births columns,
If the month value already exists as a key in births_per_month, the births value is added to the existing value,
If the month value doesn't exist as a key in births_per_month, it's created and the associated value is the births value.
After the loop, return the births_per_month dictionary.
Use the month_births() function to calculate the monthly totals for the dataset and assign the result to cdc_month_births. Display the dictionary.
'''

def readcsv(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        int_fields = []
        rows = infile.read()
        rows_list = rows.split('\n')
        for item in rows_list[1:]:
            int_fields.append(list(map(int,item.split(','))))
        return int_fields

def month_births(data):
    births_per_month = {}
    for item in data:
        month = item[1]
        births = item[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_list = readcsv('data/US_births_1994-2003_CDC_NCHS.csv')
print(month_births(cdc_list))

