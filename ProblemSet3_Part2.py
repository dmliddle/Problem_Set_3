#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)
#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)
