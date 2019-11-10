## % formating

name = "Aung Aung"
age = 28

print("Hello, %s." % name)

print("Hello, %s. You are %s." % (name, age))

## str.format()

# print("Hello, {}. You are {}.".format(name, age))

# print("Hello, {1}. You are {0}.".format(age, name))

# print("Hello, {name}. You are {age}.".format(name=name, age=age))

person = { 'name1' : name , 'age1' : age}

# print("Hello, {name}. You are {age}.".format(**person))




# Formatted String Literal

# print(f"Hello, {name}. You are {age}")

# print(F"Hello, {name}. You are {age}")

# print(F"Hello, {name.lower()}. You are {age-5}")
print(F"Hello,{person.get('name1')}. you are {person.get('age1')}")

print(
    f"Hello, {name}."
    f"You are {age}"
)
