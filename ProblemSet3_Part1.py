#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (mountain + ", sometimes\ncalled " + nickname +", ")
print ("is " + str(elevation) +"\'above sea level." )

#%% Task 2 - Lists and Iteration

# Step 1: Assign data_folder to a string
data_folder = "W:\\859_data\\triangle"

# Step 2: Create a list called data_list with string objects
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

# Step 3: Assign user_item to "roads.shp"
user_item = "roads.shp"

# Step 4: Add the user_item to the data_list
data_list.append(user_item)

# Step 5: Loop through each item in the data_list and print the full Windows path
for item in data_list:
    print(data_folder + "\\" + item)