# Please write a function named seven_brothers.
#  When the function is called, it should print out the names of the seven brothers in alphabetical order, as in
# the example below. See the similarly named exercise in part 1 for more details about the brothers.


# Write your solution here
def seven_brothers():
    brothers = ['Aapo', 'Eero', 'Juhani', 'Lauri', 'Simeoni', 'Timo', 'Tuomas']
    

    brothers.sort()

    for i in brothers:
        print(i)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    seven_brothers()