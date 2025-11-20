import json

json_string = '''{
  "id": 0,
  "idBook": 0,
  "firstName": "string",
  "lastName": "string"
}'''


person = json.loads(json_string)


def modify_person(key, value):
    if key in person:
        person[key] = value

modify_person("firstName", "João")
modify_person("lastName", "Silva")


updated_json = json.dumps(person, indent=2)
print(updated_json)
