import random


def forest():
    while True:
        answer = input("The humming sound of a river is coming from the left and there is dense forest "
                       " of oak to the right. Which way would you like to go?(left/right) ")
        if answer == "left":
            print("There is bunch of tress which can used to create firewood.")
            while True:
                answer = input("Would like to cut the trees or collect water from the "
                               "river?(cut/river) ")
                if answer == 'cut':
                    answer = input("You have collect the wood for a fire and shelter. Would you like to go build a "
                                   " shelter near the river or the coastline?(river/coastline) ")
                    while True:
                        if answer == 'river':
                            print("Numerous hippos were near the river and you were spotted.You were killed by "
                                  "the hippos.")
                            return 'Game over.'
                        elif answer == 'coastline':
                            print("You have come to the coastline. You have started to create a shelter.")
                            while True:
                                answer = input("You have created a shelter. Would you like to create a fire?(y/n)")
                                if answer == 'y':
                                    print("The fire has been lighted. You are safe for the night, ate your"
                                          " food and slept for the night.")
                                    while True:
                                        answer = input("Do you now go back the forest and bring "
                                                       "some wood or some ship to  show up in the horizon?(wood/ship) ")
                                        if answer == 'ship':
                                            print("It's day two all your food is finished and no ship has been viewed."
                                                  " There was a large tremor and the island sank.")
                                            return 'Game over, You died.'
                                        elif answer == 'wood':
                                            while True:
                                                answer = input("You have collected the wood. Would like to build a raft"
                                                               " or wait for some sign of a ship?(build/wait) ")
                                                if answer == 'build':
                                                    print("You have built the raft and set the sail. You were rescued "
                                                          "by a merchant chip.")
                                                    return 'Well done, you have escaped the island.'
                                                elif answer == 'wait':
                                                    print("It's day two all your food is finished and no ship has been "
                                                          "viewed. was a large tremor and the island sank.")
                                                    return 'Game over, You died.'
                                                else:
                                                    print("Invalid answer")
                                        else:
                                            print("Invalid answer")
                                elif answer == 'n':
                                    print("As you didn't light a fire some animal hunted you. You are dead.")
                                    return 'Game over, You are dead'
                                else:
                                    print("Invalid answer")
                        else:
                            print("Invalid answer")
                elif answer == 'river':
                    print("You collected the water and drank it. You had a severe stomach ache and died.")
                    return 'Game over, You died.'
                else:
                    print("Invalid answer")
        elif answer == "right":
            print("There is bunch of tress which can used to create firewood.")
            while True:
                answer = input("Would you like to cut the wood as firewood or collect"
                               " water from the river?(firewood/water) ")
                if answer == 'firewood':
                    while True:
                        answer = input(
                            "You have collect the wood for a fire and shelter. Would you like to go build a shelter "
                            "near the river or the coastline?(river/coastline) ")
                        if answer == 'river':
                            print("Numerous hippos were near the river and you were spotted"
                                  ".You were killed by the hippos.")
                            return 'Game over.'
                        elif answer == 'coastline':
                            print("You have come to the coastline. You have started to create a shelter.")
                            while True:
                                answer = input("You have created a shelter. Would you like to create a fire?(y/n)")
                                if answer == 'y':
                                    print("The fire has been lighted. You are safe for the night, ate your"
                                          " food and slept for the night.")
                                    while True:
                                        answer = input(
                                            "Do you now go back the forest and bring some wood or some ship to show "
                                            " up in the horizon?(wood/ship) ")
                                        if answer == 'ship':
                                            print("It's day two all your food is finished and no ship has been viewed."
                                                  " There was a large tremor and the island sank.")
                                            return 'Game over, You died.'
                                        elif answer == 'wood':
                                            while True:
                                                answer = input("You have collected the wood. Would like to build a raft"
                                                               " or wait for some sign of a ship?(build/wait) ")
                                                if answer == 'build':
                                                    print("You have built the raft and set the sail. You were rescued "
                                                          "by a merchant chip.")
                                                    return 'Well done, you have escaped the island.'
                                                elif answer == 'wait':
                                                    print("It's day two all your food is finished and no ship has been "
                                                          "viewed. There was a large tremor and the island sank.")
                                                    return 'Game over, You died.'
                                                else:
                                                    print("Invalid answer")
                                        else:
                                            print("Invalid answer")

                                elif answer == 'n':
                                    print("As you didn't light a fire some animal hunted you. You are dead.")
                                    return 'Game over, You are dead'
                                else:
                                    print("Invalid answer")
                        else:
                            print("Invalid answer")
                elif answer == 'water':
                    answer = input("Would like to go back to the coastline or explore by the river?(river/coastline) ")
                    while True:
                        if answer == 'river':
                            print("Numerous hippos were near the river "
                                  "and you were spotted.You were killed by the hippos.")
                            return 'Game over.'
                        elif answer == 'coastline':
                            print("Night has fallen. You have neither shelter nor fire. A animal hunted you and you "
                                  "died.")
                            return 'Game over, you died.'
                        else:
                            print("Invalid answer.")
                else:
                    print("Invalid answer!!")
        else:
            print("Invalid answer.")


def west():
    fate = {'removed': "You have removed the debris but you don't have much time.",
            'not_removed': "You couldn't remove the debris in time and the island started to sank."}
    while True:
        answer = input(
            "You walked quite a long time towards the west of the island. There several tress just on "
            "the outskirts of the forest. Do you like to visit "
            "the forest or walk forward?(forest/walk) ")
        if answer == 'forest':
            forest()
        elif answer == 'walk':
            while True:
                answer = input(
                    "You walked forward and found some some small tress. Do you take them or leave them?"
                    "(take/leave) ")
                if answer == 'take':
                    print("You took the plants and wasted a lot of time. Night fall and you were "
                          " hunted.")
                    return "Game over!! You died."
                elif answer == 'leave':
                    print("Night is falling. You hear the growls of some animals."
                          " At a distance you saw small cave.")
                    while True:
                        answer = input("Do you wish to stay in the cave for the night or"
                                       " stay outside and light a fire by using the tress nearby?(fire/cave) ")
                        if answer == 'cave':
                            print("You went inside the cave. The cave was empty and no animal was living"
                                  "inside. You went to sleep inside the cave. There was large tremor and the "
                                  " exit was blocked.")
                            while True:
                                answer = input("You have no vision inside the cave. What do you do now?"
                                               " Remove the debris or give up?(remove/give up) ")
                                if answer == 'give up':
                                    print("You have given up and in the morning the island sank.")
                                    return "Game over, you died."
                                elif answer == 'remove':
                                    my_fate = random.choice(list(fate.items()))
                                    key, val = my_fate[0], my_fate[1]
                                    if key == "removed":
                                        print(val)
                                        while True:
                                            answer = input("Coming out from the cave you saw some waste a few "
                                                           "metres away. Do you go and observe the waste or "
                                                           "go towards the East of the island? Remember time "
                                                           "is valuable.(waste/East) ")
                                            if answer == 'waste':
                                                while True:
                                                    answer = input("You saw some big gallons of plastic bottles"
                                                                   " and some nylon clothing in the waste. "
                                                                   "What would you like to do now? (Walk East/"
                                                                   " some non-reliable raft) ")
                                                    if answer == 'some non-reliable raft':
                                                        print("You created a raft in time and set sail."
                                                              " You were rescued by a merchant ship.")
                                                        return "You escaped the island."
                                                    elif answer == 'East':
                                                        print(
                                                            "You started walking towards the East. "
                                                            "You heard a large tremor and a rock came "
                                                            "flying towards you.")
                                                        return "Game over!! You died."
                                                    else:
                                                        print("Invalid answer!!")
                                            elif answer == 'East':
                                                print("You started walking towards the East. You heard a large"
                                                      " tremor and a rock came flying towards you.")
                                                return "Game over!! You died."
                                            else:
                                                print("Invalid answer")
                                    else:
                                        print(val)
                                        return "Game over!! You died."

                                else:
                                    print("Invalid answer!!")
                        elif answer == 'fire':
                            print("You started lighting the fire. You heard growls but "
                                  "no animal attacked you. At one point you fell asleep."
                                  " The fire was extinguished. A carnivore attacked you"
                                  " and you died.")
                            return "Game over!! You died."
                        else:
                            print("Invalid answer!!")
                else:
                    print("Invalid answer!!")
        else:
            print("Invalid answer!!")


def coastline():
    while True:
        answer = input("Which direction would like to explore first?(East/West) ")
        if answer == 'east':
            print("You have walked quite a while now. There are several rows of coconut tress.")
            while True:
                answer = input("You have spotted a tribe ahead. What would like to do?(Communicate/Run away) ")
                if answer == 'communicate':
                    while True:
                        print("You tried to communicate to the tribe. They feel threatened but soon "
                              " understand a measly person like you can't hurt them. They offered you to "
                              "stay with them for the night. You noticed they were quite an aggressive tribe.")
                        answer = input("Do you stay with them for the night or leave?(stay/leave)")
                        if answer == "stay":
                            while True:
                                print("You stayed for the night with the tribe. You offered them"
                                      " the food you were given. They became amazed and happy with your gifts.")
                                answer = input("The tribe men have small boats. Would you like to ask them for"
                                               " a boat for someone like you can't escape the apocalypse or you "
                                               "wanna be batman and go on your own?(ask/batman) ")
                                if answer == 'batman':
                                    print("You couldn't escape the island on time. You died.")
                                    return 'Game over, You died.'
                                elif answer == 'ask':
                                    print("They, people who are going to die within a couple hours graciously "
                                          "provided you with a boat. You escaped the island.")
                                    return "You survived."
                                else:
                                    print("Invalid answer!!")
                        elif answer == "leave":
                            print("You tried to go on your own. Night falls. Without shelter you were hunted"
                                  " by wild preys.")
                            return "Game over. You died."
                        else:
                            print("Invalid answer!!")
                elif answer == 'run away':
                    while True:
                        answer = input("You run away from the tribe. Which way would you like "
                                       "to go now?(forest/west side) ")
                        if answer == "forest":
                            return forest()
                        elif answer == "west side":
                            return west()
                        else:
                            print("Invalid answer.")
                else:
                    print("Invalid answer!!")
        elif answer == 'west':
            return west()
        else:
            print("Invalid answer")


def island(name):
    print(f"{name}, you have been dropped on an island which you need to escape in 2 days. The island "
          f"is inhabited by different carnivores. You have food, water, knife for two days. Your goal is"
          f" to escape anyway as possible within the next two days otherwise the island will sink.")
    while True:
        answer = input(f"There is a forest just in front of you. Would like to explore the forest or explore near the "
                       f"coastline?(forest/coastline) ")
        if answer == 'forest':
            res = forest()
            return res
        elif answer == 'coastline':
            res = coastline()
            return res
        else:
            print("Invalid answer please try again.")


def adventure():
    name = input("Please, enter your name: ")
    print(f"We welcome you to this adventure, {name}.")
    print("Let the adventure begin!!")
    print()
    res = island(name)
    print(res)


adventure()
