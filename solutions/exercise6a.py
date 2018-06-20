'''
Write a function that can calculate the min and max values for any dictionary that's passed in.
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

def max_value(input_map):
    max_key = min(list(input_map))
    max_count = input_map[list(input_map)[0]]
    for key, value in input_map.items():
        if value > max_count:
            max_key = key
            max_count = value
    return max_key

def min_value(input_map):
    min_key = min(list(input_map))
    min_count = input_map[list(input_map)[0]]

    for key, value in input_map.items():
        if value < min_count:
            min_key = key
            min_count = value
    return min_key

cdc_list = readcsv('data/US_births_1994-2003_CDC_NCHS.csv')
cdc_year_births = calc_counts(cdc_list, 0)
max_cdc_year_birth = max_value(cdc_year_births)
min_cdc_year_birth = min_value(cdc_year_births)
print(cdc_year_births)
print(max_cdc_year_birth)
print(min_cdc_year_birth)