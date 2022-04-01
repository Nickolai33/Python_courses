# 1. Выведите значение возраста из словаря person.
person = {"name": "Kelly", "age": 25, "city": "New york"}
print(person["age"], '\n')

print(person.pop("name"))



key = "age"
if key in person:
    print(person, '\n')
s = key in person
print(s, '\n')





print(person["city"])