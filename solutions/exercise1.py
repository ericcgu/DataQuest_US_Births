#Read the CSV file "US_births_1994-2003_CDC_NCHS.csv" into a string.
#Split the string on the newline character ("\n").
#Display the first 10 values in the resulting list.

f = open('data/US_births_1994-2003_CDC_NCHS.csv', 'r')
data = f.read()
data_list = data.split('\n')
print(data_list[:11])
