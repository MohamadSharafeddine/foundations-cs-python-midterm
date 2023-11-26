import requests
tabs = [{'Title': 'Google', 'URL': 'https://www.google.com/', 'Nested Tabs': []}, {'Title': 'facebook', 'URL': 'https://www.facebook.com/', 'Nested Tabs': []}]

def displayMenu():
    print("1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Sort All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")

def openTab():
    title = input("Enter tab's title: ")
    url = input("Enter tab's URL: ")
    new_tab = {}
    new_tab["Title"] = title
    new_tab["URL"] = url
    new_tab["Nested Tabs"] = []
    tabs.append(new_tab)
    global last_opened_tab
    last_opened_tab = title
    print(f"{title} opened.")
    print(tabs)
    print(last_opened_tab)

def closeTab():
    index = input("Enter index of the tab you'd like to close: ")
    if index == "":
        index = last_opened_tab
        print(last_opened_tab)
        print("test")
        for i in range(len(tabs)):
            if tabs[i].get("Title") == last_opened_tab:
                del tabs[i]
                break
    else:
        index = int(index)
        tabs.pop(index)
    print(tabs)

def switchTab():
    index = input("Enter index of the tab you'd like to display its content: ")
    if index == "":
        index = last_opened_tab
        for i in range(len(tabs)):
            if tabs[i].get("Title") == last_opened_tab:
                r = requests.get(tabs[i].get("URL"))
    else:
        index = int(index)
        tab = tabs[index]
        r = requests.get(tab.get("URL"))
    print(r.content) 
    
def displayAllTabs():
    for tab in tabs:
        print(tab.get("Title"))
        if len(tab.get("Nested Tabs")) > 1:
            print(f"    {tab.get("Nested Tabs")}")

def openNestedTab():
    index = input("Enter index of the tab you'd like to insert this tab in: ")
    if index == "":
        index = -1
    else:
        index = int(index)
    

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