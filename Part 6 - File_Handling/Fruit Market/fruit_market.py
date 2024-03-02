def read_fruits() -> dict:

    fruits_dictionary = {}

    with open("fruits.csv") as fruits:
        for line in fruits:

            line = line.replace("\n", "")
            fruitItem = line.split(";")

            fruits_dictionary[fruitItem[0]] = float(fruitItem[1])


    return fruits_dictionary


