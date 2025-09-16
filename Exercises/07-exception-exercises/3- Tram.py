# Tram

def get_travells():
    while True:
        try:
            travells = int(input("How many times do you take tram in one month?: "))
            if travells < 0 or travells > 100:
                raise ValueError("Number of times you take tram must be between 0 and 100")
            return travells
        except ValueError as err:
            print(err)

def get_ticket_cost():
    while True:
        try:
            cost = int(input("How much does one ticket cost? (kr): "))
            if cost < 0 or cost > 100:
                raise ValueError("One ticket must cost between 0 and 100 kr")
            return cost
        except ValueError as err:
            print(err)

def get_month_card_cost():
    while True:
        try:
            cost = int(input("How much does one month card cost? (kr): "))
            if cost < 0:
                raise ValueError("Card must cost more than 0 kr")
            return cost
        except ValueError as err:
            print(err)

def main():
    travells = get_travells()
    ticket_cost = get_ticket_cost()
    month_card_cost = get_month_card_cost()

    ticket_total_cost = travells * ticket_cost
    print(f"\nCost with one-time tickets: {ticket_total_cost} kr")
    print(f"Cost with monthly card: {month_card_cost} kr")

    if ticket_total_cost > month_card_cost:
        print("\nIt's worth to buy a monthly card")
    elif ticket_total_cost < month_card_cost:
        print("\nIt's not worth to buy a monthly card")
    else:
        print("\nTotal cost of tickets and montly card fee are equal")

main()