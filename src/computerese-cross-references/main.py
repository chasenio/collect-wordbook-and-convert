import click


from word.data import Word
from word.utils import save_with_arr


@click.command()
@click.argument('file', type=click.Path(exists=True))
def main(file: str):
    words = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line_text = line.strip()
            if not line_text.startswith("-"):
                continue

            word_arr = line.strip().split("，")
            word_text = word_arr[0]
            if len(word_arr) < 2:
                word_arr = line.strip().split(" ")
                last_word = word_arr[-1]
                english = word_arr[:-1]
                word_arr = [english, last_word]

            word = Word(
                word=word_text[2:],
                meaning=word_arr[1],
            )

            # though the first word is number, we get the second word
            words.append(word.word)  # english words

    new_file = f"{file}.final"
    save_with_arr(new_file, words)  # only english words


if __name__ == '__main__':
    main()
