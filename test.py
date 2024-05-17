from Char import Char

c = Char(strength=25)

#print(c.strength)
#print(c.stealth)

d = {"data": {"name": "Andrew", "surname": "Header"}}


def c(data):
    data=data["data"]
    name = data["name"]
    return name


print(c(d))
