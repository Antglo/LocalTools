#Antonio Taboas 7/13/2023
#This tool will be used to calculate my mileage between schools


# schools = ("barnes","beddingfield","central office","daniels",
            "darden","elm city","frederick","fike","forest hills","gardners",
            "hearne","hunt","jones","lee woodard","lucama","new hope",
            "operations","rock ridge","speight","springfield","stantonsburg",
            "toisnot","vick","vinson-bynum","wells","wilson early college","winstead")


#Prompt user for starting point and destination
start_school = str(input("Enter the starting school: "))
dest_school = str(input("Enter the destination: "))

#Function to initialize starting point
def start():
    if start_school in schools:
        print("Starting... " + start_school.upper())
        return start_school
    else:
        print("Please choose a valid option.")
        
#Function to initialize destination
def dest():
    if dest_school in schools:
        print("Destination... " + dest_school.upper())
        return dest_school
    else:
        print("Please choose a valid option.")

#The following combines the users inputs
if start_school.lower() and dest_school.lower() in schools:
    combine_schools = str(start_school.upper()) + str(dest_school.upper())
    print(combine_schools)
    

#Create the worlds longest keypair dictionary
# mileage = {"BARNESBEDDINGFIELD":"5", "CENTRAL OFFICE":"2", "BARNESDANIELS":"2",
           "BARNESDARDEN":""}

#The following finds and prints the mileage
# for i in mileage.keys():
    # if combine_schools == i:
        print("The amount of miles is: " + mileage.get(combine_schools))




        
if __name__ == "__main__":
    start()
    dest()