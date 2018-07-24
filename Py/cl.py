import csv

#make def fucntions modify a csv?
#woudl it be possible to make the final final output of the code csv and only then?

phonebook = [{'first_name': 'Chris',
            'number':2404472508,
            'trigger_1': 'Monetary Value'},
            {'first_name': 'Floof',
            'number':6666666666,
            'trigger_1': 'Tasty_Tasty_Souls'}]

1: reads it in creates phonebook upon open
2: mclose probram save to a csv upon mclose


def create_entry():
    results = []
    dct = {'name': input('what is the name'), 'phone': input('What is the number')}
    phonebook.append(dct)

def name_search(q):
    results = []
    for item in phonebook:
        if q.lower() in item['first_name'].lower():
            results.append(item)
    return results

def phone_search(q):
    results = []
    for item in phonebook:
        if q.lower() in str(item['number']):
            results.append(item)
    return results

def update(q):
    print('which entry would you like to update')
    for i, item in enumerate(q):
        print(i, item)
    index = int(input(": "))
    newName = input("Enter the new name")
    newNumber = input("Enture the new number")
    phonebook[phonebook.index(q[index])] = {'first_name': newName, 'number': newNumber}
    print("Phonebook has been updated")

def remove(q):
    print('delete?')
    for i, item in enumerate(q):
        print(i, item)
    index = int(input(": "))
    phonebook.pop(phonebook.index(q[index]))

print( "create \n retrieve name \n retrieve number \n update\n delete\n")
query = input(': ')



if query == "create":
    create_entry()
elif query == "retrieve":
    thing = input('what are you looking for?: ')
    results = []
    results.extend(name_search(thing))
    results.extend(phone_search(thing))
    print(results)
elif query == "update":
    update_query = input('who would you like to update')
    results = []
    results.extend(name_search(update_query))
    results.extend(phone_search(update_query))
    update(results)
elif query == "delete":
    delete_query = input("what do you want to delete:")
    results = []
    results.extend(name_search(delete_query))
    results.extend(phone_search(delete_query))
    remove(results)
