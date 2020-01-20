class PersonClass:
    def __init__(self, name, age, gender, citizenship, religion="hindi"):
        self.name = name
        self.age = age
        self.gender = gender
        self.citizenship = citizenship
        self.religion = religion
        self.say_hello()

    def say_hello(self):
        print("Welcome, " + self.name)


Gabe = PersonClass("Gabe", 35, "men", "Hungarian", "Christian")
Anne = PersonClass("Annie", 34, "women", "Hungarian")

print(Gabe.name)
print(Gabe.age)
print(Anne.name)

print("............................................")


class Employee(PersonClass):  # inheritance

    def __init__(self, name, age, gender, citizenship, experience, assessment, study):
        super().__init__(name, age, gender, citizenship)  # need to call super class __init__ function
        self.experience = experience
        self.assessment = assessment
        self.study = study

    # experience = 4
    # assessment = 9
    # study = "computer scientist"


# instance
Leslie = Employee("Lacika", 35, "men", "Hungarian", 8, 10, "scientiest")
print(Leslie.name)
print(Leslie.study)
