# "Seitsemän veljestä" is one of the first novels ever written in 
# Finnish. It is the story of seven orphaned brothers learning to make 
# their way in the world ([read more on Wikipedia](https://en.wikipedia.org/wiki/Seitsem%C3%A4n_veljest%C3%A4)).

# This program is supposed to print out the names of the brothers in  alphabetical order, but it's not working quite right yet. 
#Please fix the program so that the names are printed in the correct order.

# `print("Simeoni")
# print("Juhani")
# print("Eero")
# print("Lauri")
# print("Aapo")
# print("Tuomas")
# print("Timo")`

# Solution 1

print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

# Solution 2
name = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
name.sort()
print(name)