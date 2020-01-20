
class Person: # class = plan for building, where house = more classes
    # member of var/field - tagvaltozok
    name = ""
    age = None
    gender = ""

    # methods - inner class defined functions
    def set_age(self, value):
        self.age = value

    def set_name(self, value):
        self.name = value

    def set_gender(self, value):
        self.name = value


# object instance - objektum példány

person1 = Person()          # példányosítás
person1.set_age(35)
person1.set_name("Gabe")
person1.set_gender("man")
print(person1.age)
print(person1.name)
print(person1.gender)

# 001# of OOO = encapsulation
'''Azt jelenti, hogy az adatstruktúrákat és az adott struktúrájú adatokat kezelő függvényeket (metódusokat) 
kombináljuk. Azokat egy egységként kezeljük, és elzárjuk őket a külvilág elől. 
Az így kapott egységeket objektumoknak nevezzük.'''
# 002# of OOO = inheritance
'''Azt takarja, hogy a meglévő objektumokból levezetett újabb objektumok öröklik a definiálásukhoz 
használt alap objektumok egyes adatstruktúráit és függvényeit, 
ugyanakkor újabb tulajdonságokat is definiálhatnak, vagy régieket újraértelmezhetnek.'''
# 003# of OOO = polymorphism
'''Egy adott tevékenység (metódus) azonosítója közös lehet egy adott objektum hierarchián belül, 
ugyanakkor a hierarchia minden egyes objektumában a tevékenységeket végrehajtó metódus implementációja
 az adott objektumra nézve specifikus lehet.'''


