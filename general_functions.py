import csv

def csv_read(file):
    with open(file, 'r', newline='') as csvread:
        reader = csv.reader(csvread, delimiter = ';')
        for row in reader:
            file_content = (','.join(row))
    csvread.close()
    return file_content

def csv_write(file, info_to_file):
    with open(file, 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter = ';')
        writer.writerow(info_to_file)
    csvwrite.close()
# put info_to_file into this format: [example1,example2,example3,]
