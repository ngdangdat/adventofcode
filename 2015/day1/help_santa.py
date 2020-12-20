MAPPING = {"(": "+1", ")": "-1"}

input_path = "input.txt"
dat = open(input_path).read().strip().split("\n")
dat = dat[0]
LIMIT = 100


def fast_eval(ip, limit=LIMIT):
    ip = ip.replace("(", MAPPING["("]).replace(")", MAPPING[")"])
    result = 0
    for i in range(0, len(ip), limit):
        result = result + eval(ip[i:i + limit])

    return result


def normal_eval(ip):
    res = 0
    for i in range(len(ip)):
        if ip[i] == "(":
            res = res + 1
        elif ip[i] == ")":
            res = res - 1
    return res


def enter_1st_basement(ip):
    res = 0
    for i in range(len(ip)):
        if ip[i] == "(":
            res = res + 1
        elif ip[i] == ")":
            res = res - 1
        if res == -1:
            break
    return i + 1


if __name__ == "__main__":
    # print(f"fast_eval=[{fast_eval(dat)}]")
    print(f"enter_1st_basement=[{enter_1st_basement(dat)}]")
