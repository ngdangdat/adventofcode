INPUT = "input.txt"
dat = [line for line in open(INPUT).read().strip().split("\n")]


def move_with_token(tuple_xy, token):
    x, y = tuple_xy
    if token == "^":
        y += 1
    elif token == "v":
        y -= 1
    elif token == ">":
        x += 1
    elif token == "<":
        x -= 1

    return x, y


def calculate_number_of_houses(ip):
    mapping = dict()
    x, y = 0, 0
    mapping[f"{x}_{y}"] = 1
    for i in range(len(ip)):
        token = ip[i]
        x, y = move_with_token((x, y), token)
        key = f"{x}_{y}"
        curr_val = mapping.setdefault(key, 0)
        mapping[key] = curr_val + 1
    return len(mapping.keys())


def deliver_with_robot(ip):
    mapping = dict()
    x_santa, y_santa = 0, 0
    x_robot, y_robot = 0, 0
    mapping[f"{x_santa}_{y_santa}"] = 1
    for i in range(len(ip)):
        key = None
        token = ip[i]
        if i % 2:
            x_santa, y_santa = move_with_token((x_santa, y_santa), token)
            key = f"{x_santa}_{y_santa}"
        else:
            x_robot, y_robot = move_with_token((x_robot, y_robot), token)
            key = f"{x_robot}_{y_robot}"
        curr_val = mapping.setdefault(key, 0)
        mapping[key] = curr_val + 1

    return len(mapping.keys())


if __name__ == "__main__":
    ip = dat[0]
    print(f"calculate_number_of_houses=[{calculate_number_of_houses(ip)}]")
    print(f"deliver_with_robot=[{deliver_with_robot(ip)}]")
