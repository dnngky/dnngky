pet_list = []
pet_number = int(input("Now, how many pets would you like to have? "))

while pet_number > 0:
    pet = {}
    pet["name"] = input("What type of animal is your pet? (Cat/Dog)? ").lower()
    pet["type"] = input("What is this {} called? "
                        .format(pet["name"]))
    pet["room"] = input("Where is {} right now? (Living Room/Kitchen/Garden) "
                        .format(pet["name"])).lower()
    pet["hunger"] = float(input("What is {}'s hunger value? "
                                .format(pet["name"])))
    pet["happiness"] = float(input("What is {}'s happiness value? "
                                   .format(pet["name"])))
    if pet["type"] == "dog":
        pet["joy"] = "Woof"
        pet["angry"] = "Grrrrrr"
    else:
        pet["joy"] = "Meow"
        pet["angry"] = "Hisssss"
    pet_list.append(pet)
    pet_number -= 1
