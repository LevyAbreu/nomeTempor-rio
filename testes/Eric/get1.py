data = [
    {
        "id": 0,
        "idBook": 0,
        "firstName": "string",
        "lastName": "string"
    }
]



def add_item(id, id_book, first_name, last_name):
    new_item = {
        "id": id,
        "idBook": id_book,
        "firstName": first_name,
        "lastName": last_name
    }
    data.append(new_item)


add_item(1, 1, "João", "Silva")


print(data)
