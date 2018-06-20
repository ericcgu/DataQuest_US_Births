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

