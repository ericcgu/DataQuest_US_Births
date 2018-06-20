'''
Create a function named calc_counts() that:
Takes two, required parameters:
data: a list of lists
column: the column number we want to calculate the totals for
Populates and returns a dictionary containing the total number of births for each unique value in the column at position column.
Use the calc_counts() function to:
Return the yearly totals for the dataset and assign the result to cdc_year_births.
Return the monthly totals for the dataset and assign the result to cdc_month_births.
Return the day-of-month totals for the dataset and assign the result to cdc_dom_births.
Return the day-of-week totals for the dataset and assign the result to cdc_dow_births.
'''

def readcsv(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        int_fields = []
        rows = infile.read()
        rows_list = rows.split('\n')
        for item in rows_list[1:]:
            int_fields.append(list(map(int,item.split(','))))
        return int_fields

def calc_counts(data, column_index):
    sums_dict = {}
    for item in cdc_list:
        column_value = item[column_index]
        births = item[4]
        if column_value in sums_dict:
            sums_dict[column_value] += births
        else:
            sums_dict[column_value] = births
    return sums_dict

cdc_list = readcsv('data/US_births_1994-2003_CDC_NCHS.csv')
cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)

print(cdc_year_births)
print(cdc_month_births)
print(cdc_dom_births)
print(cdc_dow_births)
