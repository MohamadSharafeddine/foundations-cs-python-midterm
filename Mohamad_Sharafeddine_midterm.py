import requests
tabs = [{'google': 'https://www.google.com/'}]

def displayMenu():
    print("1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Sort All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")

def openTab():
    title = input("Enter tab's title: ")
    url = input("Enter tab's URL: ")
    new_tab = {title:url}
    tabs.append(new_tab)
    print(f"{title} opened")
    print(tabs)

def closeTab():
    index = input("Enter index of the tab you'd like to close: ")
    if index == "":
        index = -1
    else:
        index = int(index)
    tabs.pop(index)
    print(tabs)

def switchTab():
    index = input("Enter index of the tab you'd like to display its content: ")
    if index == "":
        index = -1
    else:
        index = int(index)
    tab = tabs[index]
    for key, value in tab.items():
        r = requests.get(value)
    print(f"{key}: ")
    print(r.content) 
    
    

def displayAllTabs():
    pass

def openNestedTab():
    pass

def sortAllTabs():
    pass

def saveTabs():
    pass

def importTabs():
    pass

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