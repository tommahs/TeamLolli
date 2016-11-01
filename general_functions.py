import csv

# Made some changes to the csv_read, it only returned 1 line, now it appends the rows to a list -> returns a list containing the complete rows
def csv_read(file):
    import csv
    file_content = []
    with open(file, 'r', newline='') as csvread:
        reader = csv.reader(csvread, delimiter = ';')
        for row in reader:
            file_content.append(row)
        csvread.close()
    return file_content

def csv_write(file, info_to_file):
    import csv
    with open(file, 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter = ';')
        writer.writerow(info_to_file)
    csvwrite.close()
# put info_to_file into this format: [example1,example2,example3,]




def inputquestion(comment):
    Input = input("{} : ".format(comment))
    return Input
