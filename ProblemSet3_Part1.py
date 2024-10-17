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

# Step 5: Loop through each item and print full path
for item in data_list:
    print(data_folder + "\\" + item)

#%% Task 3

# Step 1: Create empty string variable 'user_numbers'
user_numbers = []

# Step 2: Create for loop to let the user add integers to the string variable
for x in range(3):
    y = int(input('Enter an integer: '))
    user_numbers.append(y)

# Step 3: Sort the user_numbers string variable
user_numbers.sort()

# Step 4: Print the highest value of user_numbers
print(user_numbers[-1])

# Task 3 - Challenge

# Step 1: Create empty string variable 'userNumbers'
userNumbers = []

# Step 2: Create for loop to let the user add integers to the string variable
for x in range(3):
    y = int(input('Enter an integer: '))
    userNumbers.append(y)

# Step 3: Sort the userNumbers string variable
userNumbers.sort(reverse = True)

# Step 4: Print the highest value of userNumbers
print(userNumbers)

