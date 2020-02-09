class PersonClass:
    def __init__(self, name, age, gender, citizenship, religion="Hindi"):       # ha van default érték, akkor azt lent nem kell megadni, de átírható
        self.name = name
        self.age = age
        self.gender = gender
        self.citizenship = citizenship
        self.religion = religion
        self.say_hello()

    def say_hello(self):
        print("Welcome, " + self.name + "!","You are:", self.age, "year old,", self.gender, ",", self.citizenship, ",", self.religion)


Gabe = PersonClass("Gabe", 35, "Men", "Hungarian", "Christian")
Anne = PersonClass("Annie", 34, "Women", "Hungarian")

print("*********************************************************************")

print(Gabe.name)
print(Gabe.age)
print(Gabe.gender)
print(Gabe.citizenship)
print(Gabe.religion)

print("............................................")


class Employee(PersonClass):  # inheritance, from 1st class (öröklődés)

    def __init__(self, name, age, gender, citizenship, experience, assessment, study):
        super().__init__(name, age, gender, citizenship)                # need to call super class __init__ function
        self.experience = experience
        self.assessment = assessment
        self.study = study

    # experience = 4                             # ezek a gyerek osztály extra tagváltozói, csak az Employee-re vonatkoznak
    # assessment = 9
    # study = "computer scientist"


# object instance = objektum példány
Leslie = Employee("Lacika", 35, "men", "Hungarian", 8, 10, "scientiest")    # itt örökölte a Leslie Employee a PersonClass összes tulajdonságát
print(Leslie.name)
print(Leslie.study)
