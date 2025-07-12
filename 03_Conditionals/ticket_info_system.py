#Ticket info system for a railway app
seat_type = input("Enter seat type (sleeper/AC/general/luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air Conditioned, comfy ride")
    case "general":
        print("General: Cheapest, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")    