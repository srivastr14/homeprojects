def onBase():
    onFirst = True
    onSecond = False
    onThird = True

    list = [onFirst,onSecond,onThird]
    player_list = ['Player on First', 'Player on Second', 'Player on Third']

    if all(list):
        return "BASES LOADED"
    elif any(list):
        base_list = [i for i, x in enumerate(list) if x]
        t = [player_list[i] for i in base_list]
        return ", ".join(t)
    elif not any(list):
        return 'No one on'


print(f'Currently: {onBase()}')