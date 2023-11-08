import json


data = {

    'name': 'Jereck Orenia',
    'age': 26,
    'city': 'Lakewood, WA',
    'interests': ['Tech, Tennis, Photography, sleep'],
    'is student': True
    

}

#write data to JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('Data written to data.json.')

#Im making a change to my file to prove that I saved something.
with open('data.jason', "r") as json_file:

    print ('Data loaded form data.json:')
    print