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

#%% Task 4.3
#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
    # Check if line is data line
    if lineString[0] in ("#","u"):
        continue

    # Split the data into values
    lineData = lineString.split(",")
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[mmsi_idx] 
    #Extract the fleet value
    fleet = lineData[fleet_idx]
   # Add info to the vesselDict dictionary
    vesselDict[mmsi] = {
        'mmsi': mmsi,
        'fleet_name': fleet
    }

# Print the vesselDict to check the contents
print(vesselDict)
len(vesselDict)

#%% Task 4.4
# Step 1: Assign string value to vesselID
vesselID = "440196000"

# Step 2: Use vesselDict to lookup a matching MMSI
if vesselID in vesselDict:
    fleet_name = vesselDict[vesselID]['fleet_name']
    # Step 3: Print
    print("Vessel #" + vesselID + " flies the flag of " + fleet_name)