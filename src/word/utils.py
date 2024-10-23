from typing import List


def save_with_arr(file: str, arr: List):
    with open(file, 'w') as f:
        for word in arr:
            f.write(f"{word}\n")
        f.close()

    print(f"process done, new file: {file}")
