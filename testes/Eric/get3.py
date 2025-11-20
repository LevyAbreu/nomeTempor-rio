person = {
    "id": 0,
    "idBook": 0,
    "firstName": "string",
    "lastName": "string"
}


def update_person(id=None, id_book=None, first_name=None, last_name=None):
    if id is not None:
        person["id"] = id
    if id_book is not None:
        person["idBook"] = id_book
    if first_name is not None:
        person["firstName"] = first_name
    if last_name is not None:
        person["lastName"] = last_name


update_person(first_name="João", last_name="Silva")


print(person)
