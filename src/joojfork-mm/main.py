import click

from word.utils import save_with_arr


@click.command()
@click.argument('file', type=click.Path(exists=True))
def main(file: str):
    words = []
    lines = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line_text = line.strip()
            if '.' not in line_text:
                continue
            lines.append(line_text)  # chinese words
            # though the first word is number, we get the second word
            word_arr = line.strip().split(" ")
            words.append(word_arr[1])

    new_file = f"{file}.final"
    save_with_arr(new_file, words)  # only english words
    save_with_arr(f"{file}.chinese.txt", lines)  # english & chinese words


if __name__ == '__main__':
    main()
