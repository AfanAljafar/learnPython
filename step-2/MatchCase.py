x = int(input("Enter the order of the day : "))

match x:
    case 1:
        print("it's monday")
    case 2:
        print("it's tuesday")
    case 3:
        print("it's wednesday")
    case 4:
        print("it's thursday")
    case 5:
        print("it's friday")
    case 6:
        print("it's saturday")
    case 7:
        print("it's sunday")
    case _:
        print("order of days out of order")