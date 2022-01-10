#name
name = input("Please enter your name: ")
if " " in name:
    print("invalid spacing specified")

#beverage
beverage = input("Please enter your beverage (coffee or tea): ")

#coffee
if beverage.lower() == "coffee" or beverage.lower() == "c":
    size = input("Please enter your beverage size (small, medium or large): ")
#size
    if size.lower() == "small" or size.lower() == "medium" or size.lower() == "large" or size.lower() == "s" or size.lower() == "m" or size.lower() == "l":
        cflavour = input("Please enter your flavour (none, vanilla or chocolate): ")
#flavour
        if len(cflavour) == 0 or cflavour.lower() == "none" or cflavour.lower() == "vanilla" or cflavour.lower() == "chocolate" or cflavour.lower() == "v" or cflavour.lower() == "c":
#flavour cost
            if cflavour.lower() == "none" or len(cflavour) == 0:
                cflavour = "none"
                fcost = 0.00
            elif cflavour.lower() == "vanilla" or cflavour.lower() == "v":
                fcost = 0.25
            else:
                fcost = 0.75
#size pricing
            if size.lower() == "small" or size.lower() == "s":
                scost = 1.50
            elif size.lower() == "medium" or size.lower() == "m":
                scost = 2.50
            else:
                scost = 3.25
            print(name, ",", beverage + ",", size + ",", cflavour)
#cost calculation
            cost = round(1.13*(scost+fcost), 2)
#printing cost
            print("$", cost)
        elif len(cflavour) != 0 or cflavour.lower() != "none" or cflavour.lower() != "vanilla" or cflavour.lower() != "chocolate" or cflavour.lower() != "v" or cflavour.lower() != "c":
            print("invalid flavour input")
    elif size.lower() != "small" or size.lower() != "medium" or size.lower() != "large" or size.lower() != "s" or size.lower() != "m" or size.lower() != "l":
        print("invalid size input")

#tea
elif beverage.lower() == "tea" or beverage.lower() == "t":
    size = input("Please enter your beverage size (small, medium or large): ")
#size
    if size.lower() == "small" or size.lower() == "medium" or size.lower() == "large" or size.lower() == "s" or size.lower() == "m" or size.lower() == "l":
        tflavour = input("Please enter your flavour (none, lemon or mint): ")
#flavour
        if len(tflavour) == 0 or tflavour.lower() == "none" or tflavour.lower() == "lemon" or tflavour.lower() == "mint" or tflavour.lower() == "l" or tflavour.lower() == "m":
#flavour cost
            if tflavour.lower() == "none" or len(tflavour) == 0:
                fcost = 0.00
                tflavour = "none"
            elif tflavour.lower() == "lemon" or tflavour.lower() == "l":
                fcost = 0.25
            else:
                fcost = 0.50
#size pricing
            if size.lower() == "small" or size.lower() == "s":
                scost = 1.50
            elif size.lower() == "medium" or size.lower() == "m":
                scost = 2.50
            else:
                scost = 3.25
            print(name, ",", beverage, ",", size, ",", tflavour)
#cost calculation
            cost = round(1.13*(scost+fcost), 2)
#printing cost
            print("$", cost)
        elif len(tflavour) != 0 or tflavour.lower() != "none" or len(tflavour) != "lemon" or len(tflavour) != "mint" or len(tflavour) != "l" or len(tflavour) != "m":
            print("invalid flavour input")
    elif size.lower() != "small" or size.lower() != "medium" or size.lower() != "large" or size.lower() != "s" or size.lower() != "m" or size.lower() != "l":
        print("invalid size input")

#other beverages
else:
    print("invalid beverage input")
