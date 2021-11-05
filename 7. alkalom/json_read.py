import json
import os

data = None
with open("test.json", 'r') as data_obj:
    data = json.load(data_obj)

print(data)
print(type(data))



print(data.keys())

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

with open("kiirt_json.json", 'w') as writable_obj:
    json.dump(json.loads(json_string), writable_obj)

data = None

file_path = r"C:\WORK\Prooktatás\1. lesson"
file_name = "kiirt_json.json"
open_method = "r"

print(os.path.join(file_path, file_name))

with open(os.path.join(file_path, file_name), open_method) as data_obj:
    data = json.load(data_obj)

print(type(data))
