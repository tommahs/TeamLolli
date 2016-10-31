import csv

def csv_read(file):
    with open(file, 'r', newline='') as csvread:
        reader = csv.reader(csvread, delimiter=';')
    csvread.close()
    return reader

def csv_write(file):
    with open(file, 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter=';')
    csvwrite.close()
    return writer
