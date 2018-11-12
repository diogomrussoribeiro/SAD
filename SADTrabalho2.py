cards = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "DC", "VC", "RC", "1P", "2P", "3P", "4P", "5P",
         "6P", "7P", "8P", "9P", "10P", "DP", "VP", "RP", "1O", "2O", "3O", "4O", "5O", "6O", "7O", "8O", "9O", "10O",
         "DO", "VO", "RO", "1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "DE", "VE", "RE"]


def count_cards(my_cards):
    counted_cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for my_card in my_cards:
        for i in range(len(cards)):
            if my_card == cards[i]:
                counted_cards[i] += 1

    counted_number = counted_cards[0]

    for card_counted in counted_cards:
        if counted_number > card_counted:
            counted_number = card_counted

    if counted_number == 1:
        print("Existe ", counted_number, "baralho completo")
    else:
        print("Existem ", counted_number, "baralhos completos")


A = ["1C", "2C", "2C"]

count_cards(A)

B = ["1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E",
     "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C",
     "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"]

count_cards(B)

