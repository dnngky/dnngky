i = 1
pet_list = []

while True:
    pet_name = input("name: ")
    pet_type = input("type: ")
    pet_hunger = input("hunger: ")
    pet_happiness = input("happiness: ")
    pet_room = input("room: ")
    if pet_type == "dog":
        pet_joy = "Woof"
        pet_angry = "Grrrrrr"
    else:
        pet_joy = "Meow"
        pet_angry = "Hisssss"
    i = {"name": pet_name, "type": pet_type, "hunger": pet_hunger, \
         "happiness": pet_happiness, "room": pet_room, "joy": pet_joy, "angry": pet_angry}
    pet_list.append(i)
    add_more = input("Add more? (Y/N) ").lower()
    if add_more == "n":
        break
    elif add_more == "y":
        continue
