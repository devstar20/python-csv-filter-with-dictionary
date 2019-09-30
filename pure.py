import csv
csv_file = open("CUSTOMER_SAMPLE.CSV")
csv_reader = csv.DictReader(csv_file, delimiter=',') 
customers_sample = {}
for row in csv_reader:
	customers_sample[row["CUSTOMER_CODE"]] = 1

csv_file = open("CUSTOMER.CSV")
csv_reader = csv.DictReader(csv_file, delimiter=',') 
out_file = open("customer_out.csv", "w",  newline='\n', encoding='utf-8')
csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(csv_reader.fieldnames)

for row in csv_reader:
	if row["CUSTOMER_CODE"] in customers_sample.keys():
		csv_writer.writerow([val for val in row.values()])

csv_file = open("INVOICE.CSV")
csv_reader = csv.DictReader(csv_file, delimiter=',') 
out_file = open("invoice_out.csv", "w",  newline='\n', encoding='utf-8')
csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(csv_reader.fieldnames)

invoce_filters = {}

for row in csv_reader:
	if row["CUSTOMER_CODE"] in customers_sample.keys():
		invoce_filters[row["INVOICE_CODE"]] = 1
		csv_writer.writerow([val for val in row.values()])


csv_file = open("INVOICE_ITEM.CSV")
csv_reader = csv.DictReader(csv_file, delimiter=',') 
out_file = open("invoice_item_out.csv", "w",  newline='\n', encoding='utf-8')
csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(csv_reader.fieldnames)
for row in csv_reader:
	if row["INVOICE_CODE"] in invoce_filters.keys():
		csv_writer.writerow([val for val in row.values()])
print(customers_sample)