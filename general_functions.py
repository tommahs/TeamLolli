def csv_read(file):
    import csv
    file_content = []
    with open((file), 'r', newline='') as csvread:
        reader = csv.reader(csvread, delimiter = ';')
        for row in reader:
            file_content.append(row)
        csvread.close()
    return file_content

######
# Combining the unique sub-lists from both lists in a new list
# returning the combined list & total number of rows in the newlist
####

def combinelists(oldlst, newlst):
    combined = oldlst
    if newlst not in oldlst:
        combined.append(newlst)
    # for new in newlst:
    #     for each in oldlst:
    #         combined.append(new)
    #         if each is not new:
    #             combined.append(each)
    return combined

###
# Reading each csv file, utilize combinelists to retrieve an combined list
##
def checkdifferences(oldfile, changelist, num):
    if num == 1: #combining the unique values of each list into 1 list
        newcontent = changelist
        currentcontent = csv_read('{}.csv'.format(oldfile)) # ReadyForAck
        print('newcontent:', newcontent)
        print('currentcontent : ', currentcontent)
        combined = combinelists(currentcontent, newcontent)
        print('combined', combined)
        return combined
    if num == 2:
        currentcontent = csv_read('{}.csv'.format(changelist)) #clientlist
        combined = []
        for each in currentcontent:
            for elk in each:
                combined + each
                print(elk)
        newlst = combinelists(currentcontent, combined)
        return newlst
    # if num == 2: # removing the doubles from each list
    #     currentcontent = csv_read('{}.csv'.format(oldfile))  # ReadyForAck
    #     newcontent = csv_read('{}.csv'.format(changelist))  # Logfile
    #     newlist = dividelists(currentcontent, newcontent)
    #     return newlist

def dividelists(oldlst, logfile):
    for each in oldlst:
        for log in logfile:
            if each == log:
                print('REMOVED', each[0], each[1], each[2], each[3])
                oldlst.remove(each)
    return oldlst
######
# Write every list into a row in the csv file.
# Input has become 'filename', 'filename', 'filename' without extensions
# first filename serves as the csvwriter
# second filename serves for reading the old file
# third filename serves for reading the change file
# num = Method of use, 1 = combine, 2 = remove
# extension .csv is automatically inside the functions.
# Usage:
#
# csv_writelist('ReadyForAck', 'ReadyForAck', 'clients', 1)
# csv_writelist('ReadyForAck','ReadyForAck', 'logfile', 2)
####

def csv_writelist(file, oldfile, chlst, num):
    import csv
    writelist = checkdifferences(oldfile, chlst, num)
    with open('{}.csv'.format(file), 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter = ';')
        if num == 1:
            try:
                for eachrow in writelist:
                    writer.writerow(eachrow)
            except:
                if TypeError:
                    print('Typeerror')
        if num == 2:
            try:
                for eachrow in writelist:
                    writer.writerow(eachrow)
            except:
                if TypeError:
                    print('Typeerror')

        if num == 3:
            try:
                writer.writerow(writelist)
            except:
                if TypeError:
                    print('Typeerror')
    csvwrite.close()
# put info_to_file into this format: [example1,example2,example3,]


######
# Input question(whatever you want to ask)
####
def inputquestion(comment):
    Input = input("{} : ".format(comment))
    return Input

def create_csv_station(station_name):
    import csv
    file = open(station_name+'.csv', 'w+')
    file.close()

# if the station is in the dictionary -> give back the stationabbreviation
def stationabbreviation(station):
    stations = {'Utrecht': 'Ut',
                'Amsterdam Centraal': 'asd'}
    if station in stations:
        return stations[station]

# test voor schrijven van input naar client:
# csv_writelist('clients', 'clients', newlst, 1)
# test voor ReadyforAck bijvullen met missende lijsten
csv_writelist('ReadyForAck', 'ReadyForAck', 'clients', 2)
# csv_writelist('ReadyForAck','ReadyForAck', 'logfile', 2)

