contacts = []

with open('contact-list.csv', 'r') as file:
    lines = file.read().split('\n')
    

line_zero = lines[0].split(',')  # keys
line_one = lines[1].split(',')
line_two = lines[2].split(',')   # THESE ARE ALL STRINGS
line_three = lines[3].split(',')
line_four = lines[4].split(',')

contacts.append(line_zero)
contacts.append(line_one)
contacts.append(line_two)
contacts.append(line_three)
contacts.append(line_four)
# print(contacts)
'''
[['Name', 'Email', 'Favorite Color'], ['Jane', 'jane@company.net', 'red'], ['Bob', 'bob@company.net', 'blue'], ['Jack', 'jack@company.net', 'silver'], ['Diana', 'diana@company.net', 'yellow']]
'''

# contact_list = []
# for row in contacts:
#     contact_list = [dict(zip(line_zero, row))
# #     contact_list.append(contact)
# print(contact_list)

contact_list = [dict(zip(line_zero, row)) for row in contacts[1::]]
print(contact_list)


'''
def add(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

contacts_first = {}
contacts_second = {}
contacts_third = {}
contacts_fourth = {}

add(contacts_first, line_zero[0], line_one[0])
add(contacts_first, line_zero[1], line_one[1])
add(contacts_first, line_zero[2], line_one[2])

add(contacts_second, line_zero[0], line_two[0])
add(contacts_second, line_zero[1], line_two[1])
add(contacts_second, line_zero[2], line_two[2])

add(contacts_third, line_zero[0], line_three[0])
add(contacts_third, line_zero[1], line_three[1])
add(contacts_third, line_zero[2], line_three[2])

add(contacts_fourth, line_zero[0], line_four[0])
add(contacts_fourth, line_zero[1], line_four[1])
add(contacts_fourth, line_zero[2], line_four[2])

contacts.append(contacts_first)
contacts.append(contacts_second)
contacts.append(contacts_third)
contacts.append(contacts_fourth)
# '\n'.join(...)
# print(contacts)
'''



'''
Version 2:
-Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
-Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
-Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
-Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''
def create(line_zero, contact_list):
    add_contact = {}
    for key in line_zero:
        add_contact[key] = input(f"What is the {key} of the new contact to be added? ")
    contact_list.append(add_contact)
    print(contact_list)
    
def retrieve(line_zero, contact_list):
    retrieve_name = input("Who's contact info would you like to retrieve? ")
    for name in contact_list:
        if name['Name'] == retrieve_name:
            print(name)

def update(line_zero, contact_list):
    update_contact = input("Whose contact info would you like to update? ")
    contact_info = input("What contact piece needs to be updated? (name, email, or favorite color) ")
    updated_info = input(f"What is the updated {contact_info}? ")
    for info in contact_list:
        if info['Name'] == update_contact:
            # print(info['Name'])   # Diana
            info[contact_info] = updated_info
            # print(f"info: {info}")   # 'Name': 'Diana', 'Email': 'diana@company.net', 'Favorite Color': 'yellow', 'favorite color': 'gold'}
            return info
    print(contact_list)
        # if info['Name'] == contact_info
        # elif info['Email'] == contact_info
        # elif info['Favorite Color'] == contact_info

        # replace contact_info with updated_info


def delete(line_zero, contact_list):
    delete_contact = input("Who's contact info would you like to delete? ")
    for contact in contact_list:
        if contact['Name'] in delete_contact:
            contact_list.remove(contact)
    print(contact_list)


while True:
    user_input = input("Would you like to Create, Retrieve, Update, or Delete a record, or Finish? (c, r, u, d, f) ")
    if user_input == 'f':
        break
    elif user_input == 'c':
        create(line_zero, contact_list)
    elif user_input == 'r':
        retrieve(line_zero, contact_list)
    elif user_input == 'u':
        update(line_zero, contact_list)
    elif user_input == 'd':
        delete(line_zero, contact_list)

'''
Version 3:
When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.
'''

with open('contact-list.csv', 'w') as file:
    save_write = []
    save_write.append(list(contact_list[0].keys()))
    for contact in contact_list:
        save_write.append(list(contact.values()))
    # for x in save_write:
    #     save_write = ",".join(x)
    save_write = [','.join(x) for x in save_write]
    save_write = '\n'.join(save_write)
    # print(f"save_write: {save_write}")
    file.write(save_write)
#     file.write('\n'.join(contact_list))
# TypeError: write() argument must be str, not list
    # for x in contact_list:
    #     file.write(x)   # TypeError: write() argument must be str, not dict
    # file.close()

# write all updates from contact_list to csv