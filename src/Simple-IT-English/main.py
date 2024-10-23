import click

from word.data import Word
from word.utils import save_with_arr

"""
https://github.com/Wei-Xia/most-frequent-technology-english-words
"""


@click.command()
@click.argument('file', type=click.Path(exists=True))
def main(file: str):
    """读取指定文件, 如果 一行少于 5 个 | 则跳过"""
    words = set()
    with open(file, 'r') as fp:
        for line in fp.readlines():
            line_arr = line.split("|")
            count = len(line_arr)
            if count < 5:
                continue
            word = Word(
                word=line_arr[0].strip(),
                phonetic=line_arr[1].strip(),
                meaning=line_arr[4].strip(),
            )
            print(word)
            words.add(
                word.word
            )
    save_with_arr(f'{file}.txt', list(words))


if __name__ == '__main__':
    main()
