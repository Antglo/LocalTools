#Antonio Taboas 7/13/2023
#This tool will be used to calculate my mileage between schools

import pandas as pd

path_file = "Mileage Charts Excel.xlsx"
mile_data = pd.read_excel(path_file)
print(mile_data)
row_data = {"Barnes":0,"Beddingfield":1,"Central Office":2,"Daniels Learning Ctr.":3,"Darden":4,"Elm City Middle":5,
            "Frederick Douglass":6,"Fike":7,"Forest Hills":8,"Gardners":9,"Hearne":10,"Hunt":11,"Jones":12,	
            "Lee Woodard":13,"Lucama":14,"New Hope":15,"Operations Ctr.":16,"Rock Ridge":17,"Speight":18,"Springfield":19,"Stantonsburg":20,	
            "Toisnot":21,"Vick":22,"Vinson-Bynum":23,"Wells":24,"Wilson Early College":25,"Winstead":26}

#add everything in a loop
while True:

#Prompt user for start and destination
    start_school = str(input("Enter the starting school. Or press ENTER to quit: "))
    if start_school == '':
        break
    dest_school = str(input("Enter the destination: "))
    
#The following searches the data for the start point
    if start_school in mile_data.head(0):
        print("Start at.... " + start_school.upper())
    else:
        print("Please enter a valid Starting Point!")

#The following searches the data for the destination
    if dest_school in mile_data.head(0):
        print("Destination is.... "+ dest_school.upper())
    else:
        print("Please enter a valid Destination!")


#The following will search the data for the amount of miles
    for i in row_data.keys():
        if i == dest_school:
            chosen_key = i

    print("+-"*10,mile_data.iloc[row_data.get(chosen_key)][start_school],"MILES", "+-"*10,sep="\n", end="\n")