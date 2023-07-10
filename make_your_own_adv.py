def forest():
    while True:
        answer = input("The humming sound of a river is coming from the left and there is dense forest "
                       " of oak to the right. Which way would you like to go?(left/ right) ")
        if answer == "left":
            print("There is bunch of tress which can used to create firewood.")
            answer = input("Would you like to cut the wood as firewood or collect water from the river?(cut/river) ")
            if answer == 'cut':
                answer = input("You have collect the wood for a fire and shelter. Would you like to go build a shelter "
                               "near the river or the coastline?(river/coastline) ")
                while True:
                    if answer == 'river':
                        print("Numerous hippos were near the river and you were spotted.You were killed by the hippos.")
                        return 'Game over.'
                    elif answer == 'coastline':
                        print("You have come to the coastline. You have started to create a shelter.")
                        answer = input("You have created a shelter. Would you like to create a fire?(y/n)")
                        while True:
                            if answer == 'y':
                                print("The fire has been lighted. You are safe for the night, ate your"
                                      " food and slept for the night.")
                                answer = input("Do you now go back the forest and bring some wood or some ship to show "
                                               " up in the horizon?(wood/ship) ")
                                while True:
                                    if answer == 'ship':
                                        print("It's day two all your food is finished and no ship has been viewed."
                                              " There was a large tremor and the island sank.")
                                        return 'Game over, You died.'
                                    elif answer == 'wood':
                                        answer = input("You have collected the wood. Would like to build a raft"
                                                       " or wait for some sign of a ship?(build/wait) ")
                                        while True:
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
            elif answer == 'river':
                print("You collected the water and drank it. You had a severe stomach ache and died.")
                return 'Game over, You died.'
            else:
                print("Invalid answer")
        elif answer == "right":
            print("There is bunch of tress which can used to create firewood.")
            answer = input("Would you like to cut the wood as firewood or collect water from the river?(y/n) ")
            if answer == 'y':
                answer = input("You have collect the wood for a fire and shelter. Would you like to go build a shelter "
                               "near the river or the coastline?(river/coastline) ")
                while True:
                    if answer == 'river':
                        print("Numerous hippos were near the river and you were spotted.You were killed by the hippos.")
                        return 'Game over.'
                    elif answer == 'coastline':
                        print("You have come to the coastline. You have started to create a shelter.")
                        answer = input("You have created a shelter. Would you like to create a fire?(y/n)")
                        while True:
                            if answer == 'y':
                                print("The fire has been lighted. You are safe for the night, ate your"
                                      " food and slept for the night.")
                                answer = input("Do you now go back the forest and bring some wood or some ship to show "
                                               " up in the horizon?(wood/ship) ")
                                while True:
                                    if answer == 'ship':
                                        print("It's day two all your food is finished and no ship has been viewed."
                                              " There was a large tremor and the island sank.")
                                        return 'Game over, You died.'
                                    elif answer == 'wood':
                                        answer = input("You have collected the wood. Would like to build a raft"
                                                       " or wait for some sign of a ship?(build/wait) ")
                                        while True:
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
                        print("Numerous hippos were near the river and you were spotted.You were killed by the hippos.")
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
    pass


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

