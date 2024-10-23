import os
import click

from word.utils import save_with_arr


@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path: str):
    """读取指定目录下所有文件, 合并到一个文件, 去除重复"""
    words = set()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        with open(file_path, 'r') as fp:
            for line in fp.readlines():
                words.add(line.strip().lower())

    save_with_arr(f'{path}.txt', list(words))


if __name__ == '__main__':
    main()
