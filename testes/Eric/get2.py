class Person:
    def _init_(self, id, id_book, first_name, last_name):
        self.id = id
        self.id_book = id_book
        self.first_name = first_name
        self.last_name = last_name

    def _repr_(self):
        return f"Person(id={self.id}, id_book={self.id_book}, first_name='{self.first_name}', last_name='{self.last_name}')"


data = [
    Person(0, 0, "string", "string")
]


def add_person(id, id_book, first_name, last_name):
    new_person = Person(id, id_book, first_name, last_name)
    data.append(new_person)


add_person(1, 1, "João", "Silva")

for person in data:
   print(person)
