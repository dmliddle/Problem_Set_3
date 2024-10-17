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

#%% Task 5

#Create a Python file object, i.e., a link to the file's contents
fileObj_2 = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList_2 = fileObj_2.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj_2.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString_2"
headerLineString_2 = lineList_2[0]

#Print the contents of the headerLine
print(headerLineString_2)
#%% Task 5 Part 2

#Split the headerLineString_2 into a list of header items
headerItems_2 = headerLineString_2.split(",")

#List the index of the mmsi, shipname, and fleet_name values
transshipment_idx = headerItems_2.index('transshipment_mmsi')
s_latitude = headerItems_2.index('starting_latitude')
e_latitude = headerItems_2.index('ending_latitude')
s_longitude = headerItems_2.index('starting_longitude')
e_longitude = headerItems_2.index('ending_longitude')

#Print the values
print(transshipment_idx,s_latitude,e_latitude, s_longitude, e_longitude)

#%% Task 5 Part 3

# Examine if the ship crosses from the southern hemisphere to the northern hemisphere

#Iterate through all lines (except the header) in the data file:
for lineString_2 in lineList_2[1:]:
    # Check if line is data line
    if lineString_2[0] in ("#","u"):
        continue

    # Split the data into values
    lineData_2 = lineString_2.split(",")

    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData_2[transshipment_idx] 
    #Extract the starting latitude value
    starting_latitude = float(lineData_2[s_latitude])
        #Extract the ending latitude value
    ending_latitude = float(lineData_2[e_latitude])
        #Extract the starting longitude value
    starting_longitude = float(lineData_2[s_longitude])
        #Extract the ending longitude value
    ending_longitude = float(lineData_2[e_longitude])

    # Add boolean variable to check latitudes
    crosses_equator = starting_latitude < 0 and ending_latitude > 0
    # Add boolean variable to check longitudes
    between_long = 145 <= starting_longitude <= 155
    if crosses_equator and between_long:
        # Retrieve the fleet name from the vesselDict
        if mmsi in vesselDict:
            fleet_name = vesselDict[mmsi]['fleet_name']
            # Print the vessel's mmsi and fleet name
            print(f"Vessel #{mmsi} {starting_longitude} flies the flag of {fleet_name}")
        # BONUS
        if not any(crosses_equator and between_long for lineString_2 in lineList_2[1:]):
            print("No vessels met criteria")


   
# %%
