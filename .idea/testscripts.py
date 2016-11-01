# shallowTest to write input into clients.csv
# import custom writelist function which has 3 choices defined by the program:
# #1 combine a list and a csvfile into a list & overwrite the file with list
# #2 compare 2 csvfiles & place the unique values in a 3th list. Overwrite the file with list
# #3 compare 2 csvfiles & remove wanted values from the list, overwrite file with list
def testprocess1():
    import general_functions
    import mainclient
# Test #1 to add new tweet to clients.csv
    mainclient.clientmenu()
# Test #2 to check to combine clients.csv and ReadyForAck.csv if clientsvalue not yet known voor
    general_functions.csv_writelist('ReadyForAck','ReadyForAck', 'clients', 2)
# Test #3 to remove values in logfile from ReadyForAck
    general_functions.csv_writelist('ReadyForAck', 'ReadyForAck', 'logfile', 3)

