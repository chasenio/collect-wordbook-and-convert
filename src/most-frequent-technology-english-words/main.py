import os
import click
import yaml

from word.utils import save_with_arr
from word.data import Word
from word.data import Store

"""
https://github.com/Wei-Xia/most-frequent-technology-english-words
"""


@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path: str):
    """读取指定目录下所有文件"""
    words = set()
    store = Store()
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
            store.add(word)
    save_with_arr(f'{path}.txt', list(words))

    store.dump(f'{path}.yaml')

if __name__ == '__main__':
    main()
