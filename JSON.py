import json


data = {

    'name': 'Jereck Orenia',
    'age': 26,
    'city': 'Lakewood, WA',
    'interests': ['Tech, Tennis, Photography, sleep', 'I  yeet me repos', 'youre not about that'],
    'is student': True
}

#write data to JSON file
with open('data.json', 'w') as json_file:# w stands for writing
    json.dump(data, json_file, indent=4)#dump files it data.json with 4 indents

print('Data written to data.json.')#a confirmation message that the data has been written

#Im making a change to my file to prove that I saved something.

#create funtion to read the data form the JSON file
with open('data.json', "r") as json_file:#r stands for reading. Rreading from the Json file
    loaded_data =  json.load(json_file)#create object to load the data from the json file

#confirmation fucntion that files have been loaded
print('Data loaded form data.json:')
print(loaded_data)


#Call loaded data in the key value pair to edit
loaded_data['age'] = 27
#append into the interest array with the correct key
loaded_data['interests'].append('im secretly a filipino ninja')



#use with statement to moidify the code in the json file
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

#Print confirmation
print('Modified data to data.json file')