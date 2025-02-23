import json
import click

from word.data import Word
from word.utils import save_with_arr

"""
https://github.com/Wei-Xia/most-frequent-technology-english-words
"""


@click.command()
@click.argument('file', type=click.Path(exists=True))
def main(file: str):
    """读取指定 json 文件, 仅提取 us phone"""
    words = set()
    with open(file, 'r') as fp:
        content = json.load(fp)
        for i in content:
            word = Word(
                word=i['name'],
                meaning=i['trans'],
                phonetic=i.get('usphone'),
            )
            words.add(
                word.word
            )
    save_with_arr(f'{file}.txt', list(words))


if __name__ == '__main__':
    main()
