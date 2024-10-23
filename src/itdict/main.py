import os
import click
import yaml
from typing import List

from word.data import Word

"""
https://github.com/zionfuo/itdict
"""


def save_with_arr(file: str, arr: List):
    with open(file, 'w') as f:
        for word in arr:
            f.write(f"{word}\n")
        f.close()

    print(f"process done, new file: {file}")


@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path: str):
    """解析 程序员必学电脑计算机专业英语词汇1700词.md """
    words = []
    with open(path, 'r') as fp:
        for line in fp.readlines():
            if "<br />" not in line:
                continue
            word_arr = line.split("<br />")
            word = Word(
                word=word_arr[0].strip(),
                meaning=word_arr[1].strip(),
            )
            words.append(word.word)
    save_with_arr(f'{path}.txt', list(words))


if __name__ == '__main__':
    main()
