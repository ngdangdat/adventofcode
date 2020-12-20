import hashlib

INPUT = "iwrupvqb"
TARGET_HASH = "000000"


def find_smallest_token(ip, target_head):
    res = -1
    curr_num = 1
    while True:
        combined_str = f"{INPUT}{curr_num}"
        str_md5_in_hex = hashlib.md5(bytes(combined_str, 'utf-8')).hexdigest()
        # print(
        #     f"[DEBUG] combined_str=[{combined_str}], str_md5_in_hex=[{str_md5_in_hex}]"
        # )
        if str_md5_in_hex.startswith(target_head):
            res = curr_num
            break
        curr_num += 1
    return res


if __name__ == "__main__":
    print(f"find_smallest_token=[{find_smallest_token(INPUT, TARGET_HASH)}]")
