import json
from textwrap import indent

person = {
    "FirstName": "Jemael",
    "LastName": "Autridge",
    "Age": "18",
    "Gender": "Male"
}

person2 = {"FirstName": "Jelani", "LastName": "Autridge", "Age": "40", "Gender": "Male"}



# reads a json file and prints
with open('R&W_name.json', "r") as file:
    data = file.read()
    print(f"1. {data}")

#Creates a file and add person information to file as a json format
with open("R&W_name2.json", "w") as file:
        json.dump(person, file, indent=4)


#Converts dict to json format
data2 = json.dumps(person2, indent=4)
print(2., data2)