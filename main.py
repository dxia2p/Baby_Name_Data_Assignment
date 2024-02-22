# BABY NAMES DATA ASSIGNMENT START CODE

import json


def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    file.close()

    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL")
    for i in baby_data: # loop through all the data and print it out
        print(f"{i['name']} (Rank: {i['rank']}, Gender: {i['gender']})")

def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    print("\nSEARCH BY GENDER")
    gender = input("Enter a gender (Boy/Girl): ")
    for i in baby_data:
        if i['gender'] == gender: # only print the data if the gender matches input gender
            print(f"{i['name']} (Rank: {i['rank']}, Gender: {i['gender']})")


def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")
    minRank = int(input("Enter a minimum rank: ")) - 1 # minus one because array starts at 0
    maxRank = int(input("Enter a maximum rank: "))
    for i in range(minRank * 2, maxRank * 2): # because there are 2 names for each rank, just multiply the minimum and maximum rank by 2
        baby = baby_data[i]
        print(f"{baby['name']} (Rank: {baby['rank']}, Gender: {baby['gender']})") # print the data
    print(f"Number of names found: {maxRank * 2 - minRank * 2}") 

def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER")
    startingLetter = input("Enter a starting letter: ")
    namesFound = 0
    for i in baby_data:
        if i['name'][0] == startingLetter: # get the first character, if it is equal to the inputted starting letter then print the data
            namesFound += 1
            print(f"{i['name']} (Rank: {i['rank']}, Gender: {i['gender']})")
    print(f"Number of names found: {namesFound}")

def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
    nameLength = int(input("Enter a name length: "))
    namesFound = 0
    for i in baby_data:
        if len(i['name']) == nameLength: # if the length of the name matches input, then print the data
            namesFound += 1
            print(f"{i['name']} (Rank: {i['rank']}, Gender: {i['gender']})")
    print(f"Number of names found: {namesFound}")
# Invoke main to begin program
main()
