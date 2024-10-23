import click

from typing import List
from typing import Dict
from py_markdown_table.markdown_table import markdown_table


@click.command()
@click.argument('file', type=click.Path(exists=True))
def main(file: str):
    """https://github.com/EarsEyesMouth/computerese-cross-references"""
    with open(file, 'r') as f:
        start = False # 单词组开始结束标志
        group: List[Dict] = [] # 单词组
        for line in f.readlines():
            line_text = line.strip()
            if not line_text.startswith("-"):
                if start: # 单词组结束, 输出
                    start = False
                    markdown = markdown_table(group).set_params(row_sep = 'markdown', quote=False).get_markdown()
                    print(markdown)
                    group = []  # clear
                print(f"{line_text}") # 除单词外的其他行
                continue
            if not start:
                start = True
            # 去除 `- `
            line_text = line_text[2:]
            if "，" in line_text:
                word_arr = line_text.split("，")
            elif "," in line_text:
                word_arr = line_text.split(",")
            group.append({
                "Word": word_arr[0].strip(),
                "Meaning": "，".join(word_arr[1:]),
            })


if __name__ == '__main__':
    main()
