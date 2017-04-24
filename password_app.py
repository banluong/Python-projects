#Password generator
import random, string

# Can replace printable with string.digits and/or string.ascii_letters
# Find more when dir(string)
def generator():
    letter1 = random.choice(string.printable)
    letter2 = random.choice(string.printable)
    letter3 = random.choice(string.printable)
    letter4 = random.choice(string.printable)
    letter5 = random.choice(string.printable)
    letter6 = random.choice(string.printable)
    letter7 = random.choice(string.printable)
    letter8 = random.choice(string.printable)
    password = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8
    return(password)

#Produces 11 possible passwords to choose from
for i in range(11):
    print(generator())
