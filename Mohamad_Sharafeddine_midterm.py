# Imports
import requests
import json

# Data Structure
tabs = [{'Title': 'Google', 'URL': 'https://www.google.com/', 'Nested Tabs': []}]

# Insertion Sort, adjusted to sort based on "Title" key of a dictionary.
def insertionSort(list1): # O(n^2)
    border = 1
    while border < len(list1):
        current = border
        while current > 0 and list1[current]["Title"].lower() < list1[current - 1]["Title"].lower():
            list1[current], list1[current - 1] = list1[current - 1], list1[current]
            current -= 1
        border += 1

# Function displays menu.
def displayMenu(): # O(1)
    print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Sort All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit\n")

# Function opens a new tab.
def openTab(title, url): # O(1)
    new_tab = {}
    new_tab["Title"] = title
    new_tab["URL"] = url
    new_tab["Nested Tabs"] = []
    print(f"Opening {title}...")
    tabs.append(new_tab)
    global last_opened_tab
    last_opened_tab = title

# Function closes (deletes) the tab corresponding to the index.
def closeTab(index): # O(N), N being the length of the list.
    if "," in index:
        index_list = index.split(",")
        index_parent = int(index_list[0].strip())
        index_nested = int(index_list[1].strip())
        print("Closing", tabs[index_parent]["Nested Tabs"][index_nested]["Title"], "...")
        del tabs[index_parent]["Nested Tabs"][index_nested]
    elif index == "":
        index = last_opened_tab
        for i in range(len(tabs)):
            if tabs[i]["Title"] == last_opened_tab:
                print("Closing", tabs[i]["Title"], "...")
                del tabs[i]
                break
    else:
        index = int(index)
        print("Closing", tabs[index]["Title"], "...")
        tabs.pop(index)

# Function displays the HTML content of the tab corresponding to the index.
def switchTab(index): # O(N), N being the length of the list.
    if "," in index:
        index_list = index.split(",")
        index_parent = int(index_list[0].strip())
        index_nested = int(index_list[1].strip())
        r = requests.get(tabs[index_parent]["Nested Tabs"][index_nested]["URL"])
    elif index == "":
        index = last_opened_tab
        for i in range(len(tabs)):
            if tabs[i]["Title"] == last_opened_tab:
                r = requests.get(tabs[i]["URL"])
    else:
        index = int(index)
        tab = tabs[index]
        r = requests.get(tab["URL"])
    print(r.content) 

# Function displays all tabs including their nested tabs.
def displayAllTabs(): # O(N^2), N being the length of the list.
    print("Opened tabs: ")
    for tab in tabs:
        print(tab["Title"])
        if len(tab["Nested Tabs"]) > 0:
            for nested_tab in tab["Nested Tabs"]:
                print("  ", nested_tab["Title"])

# Function adds a nested tab to the tab corresponding to the index.
def openNestedTab(index, title, url): # O(1)
    print("Opening", title, "in", tabs[index]["Title"], "...")
    new_nested_tab = {}
    new_nested_tab["Title"] = title
    new_nested_tab["URL"] = url
    tabs[index]["Nested Tabs"].append(new_nested_tab)

# Function uses a modified Insertion Sort to sort all tabs, including nested tabs, alphabetically, based on their title.
def sortAllTabs(): # O(N^3), N being the length of the list.
    for tab in tabs: # O(N)
        insertionSort(tab["Nested Tabs"]) # O(N^2)
    insertionSort(tabs) # O(N^2)
    print("Tabs have been sorted.")

# Function writes the tabs list to the given file path in JSON format.
def saveTabs(file_path): # Source: https://www.geeksforgeeks.org/python-json/
    json_object = json.dumps(tabs, indent=4)
    with open(file_path, "w") as save_file:
        save_file.write(json_object)
    print("Tabs saved.")

# Function loads (appends) tabs from the given file path.
def importTabs(file_path): # Source: https://www.codethebest.com/python/python-read-list-of-dictionaries-from-json-file-steps/
    global tabs 
    with open(file_path) as save_file:
        loaded_tabs = json.load(save_file)
        for tab in loaded_tabs:
            tabs.append(tab)
    print("Tabs imported.")

def main():
    print("Welcome!")
    while True:
        displayMenu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            title = input("Enter Tab's Title: ").capitalize()
            while title == "":
                title = input("Enter Tab's Title (Can't be empty): ").capitalize()
            url = input("Enter Tab's URL: ").lower()
            while url == "":
                url = input("Enter Tab's URL (Can't be empty): ").lower()
            openTab(title, url)
        elif choice == 2:
            index = input("Enter index of the Tab you'd like to close (if the Tab is nested, separate it's index by a comma): ")
            closeTab(index)
        elif choice == 3:
            index = input("Enter index of the Tab you'd like to display the content of (if the Tab is nested separate it's index by a comma): ")
            switchTab(index)
        elif choice == 4:
            displayAllTabs()
        elif choice == 5:
            index = int(input("Enter index of the Tab you'd like to nest this Tab in: "))
            title = input("Enter Tab's Title: ").capitalize()
            while title == "":
                title = input("Enter Tab's Title (Can't be empty): ").capitalize()
            url = input("Enter Tab's URL: ").lower()
            while url == "":
                url = input("Enter Tab's URL (Can't be empty): ").lower()
            openNestedTab(index, title, url)
        elif choice == 6:
            sortAllTabs()
        elif choice == 7:
            file_path = input("Enter file path to save the current state of open Tabs in: ")
            saveTabs(file_path)
        elif choice == 8:
            file_path = input("Enter file path to import Tabs from: ")
            importTabs(file_path)
        elif choice == 9:
            print("Exited program.")
            break
        else:
            print("Invalid input.")

main()