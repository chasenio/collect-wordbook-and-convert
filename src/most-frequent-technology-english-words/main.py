import os
import click
import yaml
from typing import List

from word.data import Word

"""
https://github.com/Wei-Xia/most-frequent-technology-english-words
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
    """读取指定目录下所有文件"""
    words = set()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        with open(file_path, 'r') as fp:
            # 去除文本中的 ---
            content = fp.read().replace('---', '')
            data = yaml.safe_load(content)
            word = Word(
                word=data['word'],
                meaning=data['meaning'],
                phonetic=data['correct'],
                note=data['note'],
            )
            words.add(word.word)
    save_with_arr(f'{path}.txt', list(words))


if __name__ == '__main__':
    main()
