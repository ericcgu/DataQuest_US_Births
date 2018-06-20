'''
Create a function named read_csv() that:
Takes a single, required argument, a string representing the file name of the CSV file.
Reads the file into a string, splits the string on the newline character ("\n"), and removes the header row. Assign this list to string_list and create an empty list named final_list.
Uses a for loop to:
Iterate over string_list,
Create an empty list named int_fields,
Splits each row on the comma delimiter (,) and assigns the resulting list to string_fields,
Converts each value in string_fields to an integer and appends to int_fields,
Appends int_fields to final_list.
Returns final_list.
Use the read_csv() function to read in the file "US_births_1994-2003_CDC_NCHS.csv" and assign the result to cdc_list.
Display the first 10 rows of cdc_list to confirm it's a list of lists, containing only integer values, and no header row.
'''

def readcsv(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        int_fields = []
        rows = infile.read()
        rows_list = rows.split('\n')
        for item in rows_list[1:]:
            int_fields.append(list(map(int,item.split(','))))
        return int_fields

cdc_list = readcsv('data/US_births_1994-2003_CDC_NCHS.csv')
print(cdc_list[:11])

