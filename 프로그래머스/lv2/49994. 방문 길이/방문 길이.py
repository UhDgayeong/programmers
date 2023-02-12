def solution(dirs):
    road = []
    pos_x = 5
    pos_y = 5
    
    for d in dirs:
        tmp = [pos_x, -1, pos_y]
        if d == "U" and pos_y > 0:
            pos_y -= 1
            tmp.insert(2, pos_y)
        elif d == "D" and pos_y < 10:
            pos_y += 1
            tmp.append(pos_y)
        elif d == "L" and pos_x > 0:
            pos_x -= 1
            tmp.insert(0, pos_x)
        elif d == "R" and pos_x < 10:
            pos_x += 1
            tmp.insert(1, pos_x)
        else:
            continue
        road.append(tuple(tmp))

    return len(set(road))