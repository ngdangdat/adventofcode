INPUT_FILE = "input.txt"
dat = [line for line in open(INPUT_FILE).read().strip().split("\n")]

SPLIT_TOKEN = "x"


def parse_input_lwh(ip):
    nums = [int(x) for x in ip.split(SPLIT_TOKEN)]
    return nums[0], nums[1], nums[2]


def calculate_wrapper(ip):
    l, w, h = parse_input_lwh(ip)
    squares = [l * w, w * h, l * h]
    return 2 * sum(squares) + min(squares)


def calculate_ribbon(ip):
    l, w, h = parse_input_lwh(ip)
    half_distances = [l + w, w + h, l + h]
    return 2 * min(half_distances)


def calculate_bow(ip):
    l, w, h = parse_input_lwh(ip)
    return l * w * h


if __name__ == "__main__":
    wrapper_area = 0
    for line in dat:
        wrapper_area += calculate_wrapper(line)

    print(f"wrapper_area=[{wrapper_area}]")
    total_extra = 0
    for line in dat:
        total_extra += calculate_ribbon(line) + calculate_bow(line)

    print(f"total_extra=[{total_extra}]")
