class Person:
    # like constructor func.
    def __init__(self, inheritance):
        self.money = inheritance

    def buy(self, cost):
        self.money -= cost

    def earn(self, salary):
        self.money += salary


human1 = Person(100)
human1.earn(50)
human1.buy(10)
print(human1.money)

# we can use Class itself to call a method. Must to specify 'self'.
Person.buy(human1, 40)
print(human1.money)


# this will throw a Exception; "AttributeError: type object 'Person' has no attribute 'money'"
# print(Person.money)

class Money:
    locale = "unknown"

    def __init__(self, locale):
        self.locale = locale


won = Money("kr")
dollar = Money("us")
print(Money.locale)
print(won.locale)
print(dollar.locale)

print(id(Money.locale))
print(id(won.locale))
print(id(dollar.locale))
