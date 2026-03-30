environment = {
    "A": "Dirty",
    "B": "Dirty"
}


location = "A"


performance = 0

while True:
    print("Agent location:", location)
    print("Room status:", environment)

    if environment[location] == "Dirty":
        print("Action: Suck (Cleaning room)")
        environment[location] = "Clean"
        performance += 10   

    else:
     
        if location == "A":
            print("Action: Move Right")
            location = "B"
        elif location == "B":
            print("Action: Move Left")
            location = "A"

        performance -= 1  

    print("Performance score:", performance)
    print("---------------------------")

    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("All rooms are clean!")
        break
