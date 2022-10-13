from random import choice


def run_outfit_generator():
    tops = ["white square neck top", "white button down", "blue button down", "blue&white button down",
            "brown luxe tshirt",
            "green long sleeve top", "white turtleneck", "black turtleneck", "gray turtleneck", "orange peplum top",
            "gray polo"]
    bottoms = ["black pixie pants", "houndstooth pixie pants", "brown pixie pants", "blue pixie pants",
               "black flare pants",
               "blue flare pants", "black linen pants"]

    coded_tops = coding(tops)
    coded_bottoms = coding(bottoms)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    tops_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bottoms_choice = [0, 1, 2, 3, 4, 5, 6]
    print(f"\nHello Beautiful! Here are your outfits for the week!\n")
    for day in days:

        top_select = choice(tops_choice)
        if top_select == 0 or top_select == 1 or top_select == 6:
            pant_select = choice_excluding(bottoms_choice, [])

        elif top_select == 2:
            pant_select = choice_excluding(bottoms_choice, [2])

        elif top_select == 3:
            pant_select = choice_excluding(bottoms_choice, [2, 3])

        elif top_select == 4:
            pant_select = choice_excluding(bottoms_choice, [1, 2, 3, 5])

        elif top_select == 5 or top_select == 8 or top_select == 10:
            pant_select = choice_excluding(bottoms_choice, [2, 3, 5])

        elif top_select == 7:
            pant_select = choice_excluding(bottoms_choice, [0, 3, 4, 5, 6])

        elif top_select == 9:
            pant_select = choice_excluding(bottoms_choice, [0, 1, 2, 4, 6])

        print(f"On {day}, you will wear the {coded_tops[top_select]} with {coded_bottoms[pant_select]}")
        del coded_bottoms[pant_select]
        del coded_tops[top_select]
        tops_choice.remove(top_select)
        bottoms_choice.remove(pant_select)


def coding(clothes):
    coded_clothes = {}
    for num, cloth in enumerate(clothes):
        coded_clothes[num] = cloth
    return coded_clothes


def choice_excluding(lst, exception):
    possible_choices = [v for v in lst if v not in exception]
    return choice(possible_choices)


if __name__ == "__main__":
    while True:
        try:
            run_outfit_generator()
            break
        except:
            print(f"\nShit, let me retry that...")
            run_outfit_generator()
            break
