# I added more inputs for name, another verb and a preposition.

print("Please enter the following:")
print()

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
name = input("name: ")
verb4 = input("verb: ")
preposition = input("preposition: ")
print()

print("Your story is:")
print()

print(
    f'The other day, I was really in trouble. It all started when I saw a very\n{adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all\nI could think to do was to {verb2} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3}\nright in front of my family.\n{name.capitalize()} and I tried to catch the {animal} but it {verb4} {preposition} the table'
)
