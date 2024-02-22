def oldest_person(people: list)-> str:

    oldest = 2024

    for tuple_p in people:
        
        if tuple_p[1] < oldest:
            oldest = tuple_p[1]
            oldest_name = tuple_p[0]

    return oldest_name





if __name__ == "__main__":

    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))