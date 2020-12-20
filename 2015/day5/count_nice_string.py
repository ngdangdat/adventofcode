INPUT = "input.txt"
INVALIDS = ["ab", "cd", "pq", "xy"]
VOWELS = ['a', 'e', 'i', 'o', 'u']
TARGET_VOWELS_CNT = 3

dat = [line for line in open(INPUT).read().strip().split("\n")]


def contains_enough_vowels(ip):
    cnt = 0
    for i in ip:
        if i in VOWELS:
            cnt += 1
            if cnt >= TARGET_VOWELS_CNT:
                return True
    return False


def contains_double_char(ip):
    prev = None
    for c in ip:
        if prev is not None:
            if c == prev:
                return True
        prev = c
    return False


def contains_invalid(ip):
    for invalid_str in INVALIDS:
        try:
            ip.index(invalid_str)
            return True
        except ValueError:
            pass
    return False


def is_nice_1st(ip):
    if contains_invalid(line):
        return False
    if not contains_enough_vowels(line) or not contains_double_char(line):
        return False
    return True


def contains_duplication_pair(ip):
    index_mapping = dict()
    prev = None
    indexes = list()
    for idx, val in enumerate(ip):
        if prev is not None:
            key = f"{prev}{val}"
            curr_index_list = index_mapping.setdefault(key, [])
            if (idx - 1) not in curr_index_list and idx not in curr_index_list:
                curr_index_list.append(idx - 1)
                curr_index_list.append(idx)
            if len(curr_index_list) >= 4:
                return True
            index_mapping[key] = curr_index_list
        prev = val
    return False


def contains_char_dup_triplet(ip):
    for i in range(len(ip) - 2):
        start = i
        end = i + 3
        triplet = ip[start:end]
        if triplet[0] == triplet[2]:
            return True
    return False


def is_nice_2nd(ip):
    if contains_duplication_pair(ip) and contains_char_dup_triplet(ip):
        return True
    return False


if __name__ == "__main__":
    nice_strings_1st_cnt = 0
    nice_strings_2nd_cnt = 0
    for line in dat:
        if is_nice_1st(line):
            nice_strings_1st_cnt += 1
        if is_nice_2nd(line):
            print(line)
            nice_strings_2nd_cnt += 1

    print(f"nice_strings_1st_cnt=[{nice_strings_1st_cnt}]")
    print(f"nice_strings_2nd_cnt=[{nice_strings_2nd_cnt}]")
