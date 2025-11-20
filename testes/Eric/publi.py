from dataclasses import dataclass

@dataclass
class Person:
    id: int
    idBook: int
    firstName: str
    lastName: str


person = Person(id=0, idBook=0, firstName="string", lastName="string")


def print_person(p):
    print(f"ID: {p.id}, Book ID: {p.idBook}, Name: {p.firstName} {p.lastName}")


person.firstName = "João"
person.lastName = "Silva"
print_person(person)
