def solution(wallpaper):
    x_arr = []
    y_arr = []
    for x, w in enumerate(wallpaper):
        for y, cell in enumerate(w):
            if cell == "#":
                x_arr.append(x)
                y_arr.append(y)

    return [min(x_arr), min(y_arr), max(x_arr)+1, max(y_arr)+1]