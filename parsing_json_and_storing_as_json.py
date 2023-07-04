import json

json_file_name = "list_of_persons.json"

class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        

# initializing context manager for this program's json file
# also parsing the json file
with open(json_file_name, 'r') as json_file:
    data = json.load(json_file)
    
# converting the dictionaries into objects of the class, person, and storing them into a list of person objects
person_objects = []

for i in range(0, len(data)):
    current_person_dict = data[i]
    new_person_obj = person(current_person_dict["name"], current_person_dict["age"], current_person_dict["city"])
    person_objects.append(new_person_obj)

# printing out the person objects in the person objects list
for i in range(0, len(person_objects)):
    current_person_obj = person_objects[i]
    
    print("")
    print(f"Person {i + 1}: ")
    print(" " + current_person_obj.name)
    print(" " + str(current_person_obj.age))
    print(" " + current_person_obj.city)
    
# adding new persons to the list
print("You will now be inputting a new person into the list.")
new_person_name = input("New person's name: ")
new_person_age = input("New person's age: ")
new_person_city = input("New peron's city: ")
person_objects.append(person(new_person_name, new_person_age, new_person_city))

# asking the user if they want to keep adding more people
wants_to_add_another_person = True
while(wants_to_add_another_person == True):
    response = input("Do you want to add another person (y/n): ")
    if(response == "y"):
        new_person_name = input("New person's name: ")
        new_person_age = input("New person's age: ")
        new_person_city = input("New peron's city: ")
        person_objects.append(person(new_person_name, new_person_age, new_person_city))
    elif(response == "n"):
        wants_to_add_another_person = False # once set, terminates the loop
    else:
        print("Invalid response, please try again.")

    # printing out the person objects in the updated person objects list
    for person_obj in person_objects:
        print(person_obj.name)
        print(person_obj.age)
        print(person_obj.city)
        
# Writing the new version of the data into the json file
new_data = [] # list for the new data
for person_obj in person_objects:
    
    new_person_dict = {
        "name": person_obj.name,
        "age": person_obj.age,
        "city": person_obj.city
    }
    
    new_data.append(new_person_dict)

with open(json_file_name, 'w') as json_file:
    json.dump(new_data, json_file, ensure_ascii = False, indent = 4)