# json package import
# dict to json 
# json to dict
# json olvasás
# json írás
# formázás
import json

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
 
print(type(data))

# serialize python objektum JSON formázott stringé
json_string = json.dumps(data, indent=4)

# print(json_string)
# ############

# JSON string
# 
json_string = """
{ 
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives":[
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ] 
    }
}
"""

print(type(json_string))


# deserializálja
python_object = json.loads(json_string)
print(type(python_object))






#print(python_object['researcher']['relatives'][0]['name'])