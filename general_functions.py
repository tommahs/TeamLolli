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
    combined = []
    combinecounter = 0
    for eachpending in oldlst:
        combined.append(eachpending)
    if newlst not in oldlst:
        combined.append(newlst)
    return combined, combinecounter

###
# Reading each csv file, utilize combinelists to retrieve an combined list
##
def checkdifferences(oldfile, changelist, num):
    from general_functions import csv_read
    if num == 1: #combining the unique values of each list into 1 list
        newcontent = changelist
        currentcontent = csv_read('{}.csv'.format(oldfile))
        combined, combinecounter = combinelists(currentcontent, newcontent)
        return combined, combinecounter
    if num == 2: # removing the doubles from each list
        currentcontent = csv_read('{}.csv'.format(oldfile))  # ReadyforAck
        newcontent = csv_read('{}.csv'.format(changelist))  # Logfile
        newlist = dividelists(currentcontent, newcontent)
        return newlist
######
# Write every list into a row in the csv file.
# Input has become 'filename', 'filename', 'filename' without extensions
# first filename serves as the csvwriter
# second filename serves for reading the old file
# third filename serves for reading the new file
# extension .csv is automatically inside the functions.
# Usage:
# csv_write('ReadyForAck', 'ReadyForAck', 'clients')
####

def csv_writelist(file, oldfile, newlst, num):
    import csv
    writelist = checkdifferences(oldfile, newlst, num)
    with open('{}.csv'.format(file), 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter = ';')
        for eachlst in writelist:
            try:
                for each in eachlst:
                    writer.writerow(each)
            except:
                if TypeError:
                    continue
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


def finishedtweets(oldfile, logfile):
    from general_functions import csv_read
    currentcontent = csv_read('{}.csv'.format(oldfile)) #ReadyforAck
    print('curcontent', currentcontent)
    toberemovedcontent = csv_read('{}.csv'.format(logfile)) # Logfile
    newlist = dividelists(currentcontent, toberemovedcontent)
    return newlist

def dividelists(oldlst, logfile):
    try:
        print('oldlist,', oldlst)
        for each in oldlst:
                print('pak elk', each)
                if each == logfile:
                    print('REMOVED')
                else:
                    print('userless!')
                    # input()

    except:
        if ValueError:
            print('valueerror')
    return oldlst

#csv_writelist('ReadyForAck', 'ReadyForAck', 'clients', 1)
# csv_writelist('ReadyForAck','ReadyForAck', 'logfile', 2)
