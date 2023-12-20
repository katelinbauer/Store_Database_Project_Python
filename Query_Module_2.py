def query():
    import Set_Up_Module
    database_of_purchases = Set_Up_Module.database_purchases()
    while True:
        input_person = int(input("Indicate the customer whose purchases you are interested in listing: "))
        if input_person == 0:
            exit()
        if input_person not in database_of_purchases:
            print("Person", input_person, "did not make any purchases.")
            query()
        count = 0
        for element in database_of_purchases[input_person][0]:
            if isinstance(element, list):
                count += 1
        y = 0
        total = 0
        while True:
            if y < count:
                first = database_of_purchases[input_person][0][y][0]
                second = int(database_of_purchases[input_person][0][y][1])
                y = y+1
                total = total + second
                print("item #", first, "$", second)
            else:
                print("for a total of: $", total)
                break

query()



