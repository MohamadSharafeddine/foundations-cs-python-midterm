import requests
import json

tabs = [{'Title': 'Google', 'URL': 'https://www.google.com/', 'Nested Tabs': []}]

# Insertion Sort
def insertionSort(list1): #O(n^2)
    border = 1
    while border < len(list1):
        current = border
        while current > 0 and list1[current]["Title"].lower() < list1[current - 1]["Title"].lower():
            list1[current], list1[current - 1] = list1[current - 1], list1[current]
            current -= 1
        border += 1

# Function displays menu
def displayMenu():
    print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Sort All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit\n")

# Function asks for Title and URL and then opens a new tab
def openTab():
    title = input("Enter tab's title: ").capitalize()
    url = input("Enter tab's URL: ").lower()
    new_tab = {}
    new_tab["Title"] = title
    new_tab["URL"] = url
    new_tab["Nested Tabs"] = []
    print(f"Opening {title}...")
    tabs.append(new_tab)
    global last_opened_tab
    last_opened_tab = title

# Function asks for index and then deletes (closes) the corresponding tab
def closeTab():
    index = input("Enter index of the tab you'd like to close: ")
    while int(index) >= len(tabs):
        index = input(f"Index must be less than {len(tabs)}: ")
    if index == "":
        index = last_opened_tab
        for i in range(len(tabs)):
            if tabs[i]["Title"] == last_opened_tab:
                print(f"Closing {tabs[i]["Title"]}...")
                del tabs[i]
                break
    else:
        index = int(index)
        print(f"Closing {tabs[index]["Title"]}...")
        tabs.pop(index)

# Function asks for index and then displays the HTML content of the corresponding tab
def switchTab():
    index = input("Enter index of the tab you'd like to display its content: ")
    while int(index) >= len(tabs):
        index = input(f"Index must be less than {len(tabs)}: ")
    if index == "":
        index = last_opened_tab
        for i in range(len(tabs)):
            if tabs[i]["Title"] == last_opened_tab:
                r = requests.get(tabs[i]["URL"])
    else:
        index = int(index)
        tab = tabs[index]
        r = requests.get(tab["URL"])
    print(r.content) 
    
def displayAllTabs():
    print("Opened tabs: ")
    for tab in tabs:
        print(tab["Title"])
        if len(tab["Nested Tabs"]) > 0:
            for nested_tab in tab["Nested Tabs"]:
                print(f"  {nested_tab["Title"]}")

def openNestedTab():
    index = int(input("Enter index of the tab you'd like to insert this tab in: "))
    while int(index) >= len(tabs):
        index = input(f"Index must be less than {len(tabs)}: ")
    title = input("Enter tab's title: ").capitalize()
    url = input("Enter tab's URL: ").lower()
    print(f"Opening {title} in {tabs[index]["Title"]}...")
    new_nested_tab = {}
    new_nested_tab["Title"] = title
    new_nested_tab["URL"] = url
    tabs[index]["Nested Tabs"].append(new_nested_tab)

def sortAllTabs():
    for tab in tabs:
        insertionSort(tab["Nested Tabs"])
    insertionSort(tabs)
    print("Tabs have been sorted.")

def saveTabs():
    file_path = input("Enter file path to save the current state of open tabs: ")
    json_object = json.dumps(tabs, indent=4)
    with open(file_path, "w") as save_file:
        save_file.write(json_object)
    print("Tabs saved.")

def importTabs():
    global tabs 
    file_path = input("Enter file path to save the current state of open tabs: ")
    with open(file_path) as save_file:
        tabs = json.load(save_file)
    print("Tabs imported.")

def main():
    print("Welcome!")
    while True:
        displayMenu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            openTab()
        elif choice == 2:
            closeTab()
        elif choice == 3:
            switchTab()
        elif choice == 4:
            displayAllTabs()
        elif choice == 5:
            openNestedTab()
        elif choice == 6:
            sortAllTabs()
        elif choice == 7:
            saveTabs()
        elif choice == 8:
            importTabs()
        elif choice == 9:
            print("Exited program.")
            break
        else:
            print("Invalid input.")

main()