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

def replace(oldlst,newlst):
    with open(oldlst,'r') as f:
        with open(newlst,'w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)



def replace2(oldlst,newlst):
    with open(oldlst, 'r') as f4:
        with open(newlst,'w') as f5:
            for line in f4:
                f5.write(line)



def combinelists(oldlst, newlst):
    combined = oldlst
    if newlst not in oldlst:
        combined.append(newlst)
    return combined

###
# Reading each csv file, utilize combinelists to retrieve an combined list
##
def checkdifferences(oldfile, changelist, num):
    if num == 1: #combining the unique values of a list & file into 1 list
        newcontent = changelist
        currentcontent = csv_read('{}.csv'.format(oldfile)) # ReadyForAck
        combined = combinelists(currentcontent, newcontent)
        return combined
    if num == 2: # combine the unique values of 2 files into 1 list
        currentcontent = csv_read('{}.csv'.format(changelist)) #clientlist
        combined = []
        for each in currentcontent:
            # for elk in each:
                combined + each
        newlst = combinelists(currentcontent, combined)
        return newlst
    if num == 3: # removing the doubles from each list
        currentcontent = csv_read('{}.csv'.format(oldfile))  # ReadyForAck
        changecontent = changelist
        newlist = dividelists(currentcontent, changecontent)
        return newlist


# def dividelists(oldlst, logfile):
#     lst = []
#     for each in oldlst:
#         if each in logfile:
#             lst.append(each)
#             print('list:', lst)
#         else:
#             print('Logged.', each)
#     return lst
def dividelists(oldlst, tweet):
    for each in oldlst:
        if each == tweet:
            print('REMOVED', each[0], each[1], each[2], each[3])
            print('true:', each)
            oldlst.remove(each)
            print('each:', each)
        else:
            print('wut')
            pass

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
        try:
            print('writelist', writelist)
            for eachrow in writelist:
                writer.writerow(eachrow)
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


#####
# Need gui to connect the following functions with
##
def popuptext(text):
    print(text)


def accepted(eachtweet):
    import general_functions
    from authenticator import oauth
    try:
        ##
        tweet = '{}: {} #{}'.format(eachtweet[0], eachtweet[1], eachtweet[3].upper())
        r = oauth.request('statuses/update', {'status': tweet})
        # print('SUCCES' if r.status_code == 200 else 'FAILURE')
        ## input send to twitter function
        replace("clients.csv","ReadyForAck.csv")
        replace2("ReadyForAck.csv","clients.csv")
    except:
        print('ietsgaatfout')

def rejected(eachtweet):
    import general_functions
    try:
        # write to logfile
        # remove tweet from ReadyForAck
        general_functions.csv_writelist('logfile', 'logfile', eachtweet, 1)
        general_functions.csv_writelist('ReadyForAck', 'ReadyForAck', eachtweet, 3)
    except:
        "ietsgaatfout"

def openlogfile():
    csvlog = csv_read('logfile.csv')
    csvlog.reverse()
    print('name:  message: date:')
    num = 1
    if len(csvlog) >=50:
        maxnum = 50
    else:
        maxnum = len(csvlog)
    while num <= maxnum:
        for eachlst in csvlog:
            print(eachlst[0], eachlst[1], eachlst[2], eachlst[3])
            num +=1
#openlogfile()
