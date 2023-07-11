def forest():
    while True:
        answer = input("The humming sound of a river is coming from the left and there is dense forest "
                       " of oak to the right. Which way would you like to go?(left/ right) ")
        if answer == "left":
            print("There is bunch of tress which can used to create firewood.")
            while True:
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
                answer = input("Would you like to cut the wood as firewood or collect water from the river?(y/n) ")
                if answer == 'y':
                    while True:
                        answer = input(
                            "You have collect the wood for a fire and shelter. Would you like to go build a shelter "
                            "near the river or the coastline?(river/coastline) ")
                        if answer == 'river':
                            print("Numerous hippos were near the river and you were spotted.You were killed by the hippos.")
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
                                                    print("You have built the raft and set the sail. You were rescued by a "
                                                          "merchant chip.")
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
                elif answer == 'n':
                    answer = input("Would like to go back to the coastline or river?(river/coastline) ")
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
            print("Invalid answer.")


def coastline():
    answer = input("Which direction would like to explore first?(East/West) ")
    while True:
        if answer == 'east':
            print("You have walked quite a while now. There are several rows of coconut tress.")
            answer = input("You have spotted a tribe ahead. What would like to do?(Communicate/Run away) ")
            while True:
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
                                               " a boat for a someone like you can't the apocalypse or would be "
                                               "wanna batman and go on own?(ask/batman) ")
                                if answer == 'myself':
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
                else:
                    print("Invalid answer!!")
        elif answer == 'west':
            pass
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
