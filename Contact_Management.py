import json
def add_contact():
    name=input("name: ")
    age=int(input("age: "))
    phone_num=int(input("phone: "))
    contact={"name":name,"age":age,"phone_num":phone_num}
    return contact

def dis_list(people):
    for i,contact in enumerate(people):
        print(i,"-",contact)

def del_contact(people):
    dis_list(people)
    while True:
        num=int(input("Enter a valid contact number to delete contact list starts from '0': "))
        try:
            num=int(num)
            if(num<0 or num>=len(people)):
                print("contact number not present")
            else:
                break
        except:
            print("Invalid contact number")
    people.pop(num)
    print("contact deleted!")
    dis_list(people)

def search_contact(people):
    search=input("search for a contact name: ").lower()
    find=[]
    for i in people:
        nam=i["name"]
        ag=i["age"]
        ph=i["phone_num"]
        if((search in nam) or (search in str(ag)) or (search in str(ph))):
            find.append(i)
    dis_list(find)

print("Welcome To Contact Management System.")
print()

with open('contacts.json','r') as f:
    people=json.load(f)["contacts"]

if(len(people)==0):
    print("contacts are null")
else:
    dis_list(people)

print()

while True:
    command=input("You can 'add','delete','search' and 'save the contact changes in the file(by entering ''save'')' or 'quit' the contact: ").lower()
    if (command =="add"):
        contact=add_contact()
        people.append(contact) 
        print("contact added!")
        dis_list(people)
    elif (command =="delete"):
        del_contact(people)
        if(len(people)==0):
            print("contacts are null")
    elif (command =="search"):
        search_contact(people)
    elif (command =="save"):
        my_data={}
        my_data["contacts"] = people 
        json_str=json.dumps(my_data,indent=4)
        with open('contacts.json','w') as f:
            f.write(json_str) 
        print("contacts updated")
    elif (command == "quit"):
        break
    else:
        print("Invalid command!")


