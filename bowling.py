def score(game):
    result = 0
    frame = 1
    for i in range(len(game)):
        if game[i] != '/':
            result += get_value(game[i])
        if frame < 19  and get_value(game[i]) == 10:
            result += get_value(game[i+1])
            if game[i] == '/':
                result += 10 - get_value(game[i-1])
            else:
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        if game[i].lower()=='x':
            frame += 2
        else:
            frame += 1
    return result

def get_value(char):
    if char in "123456789":
        return int(char)
    elif char.lower() == 'x' or char =='/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()