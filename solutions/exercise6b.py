'''
Write a function that extracts the same values across years and calculates the differences between consecutive values to show if number of births is increasing or decreasing.
For example, how did the number of births on Saturday change each year between 1994 and 2003?
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
    for item in data:
        column_value = item[column_index]
        births = item[4]
        if column_value in sums_dict:
            sums_dict[column_value] += births
        else:
            sums_dict[column_value] = births
    return sums_dict

def calc_diffs(input_dict):
    diff_dict = {}
    keys = list(input_dict.keys())
    for key in keys[1:]:
        diff_dict[key] = input_dict[key] - input_dict[key-1]
    return diff_dict
        
cdc_list = readcsv('data/US_births_1994-2003_CDC_NCHS.csv')
cdc_year_births = calc_counts(cdc_list, 0)
print(cdc_year_births)
print(calc_diffs(cdc_year_births))
