from typing import Optional
from dataclasses import dataclass

import dacite


@dataclass
class Word:
    word: str
    meaning: Optional[str] = None  # 意思, 含义
    phonetic: Optional[str] = None  # 音标
    note: Optional[str] = None  # 笔记
    category: Optional[str] = None  # 分类

    def __hash__(self):
        return hash(self.word)

    def __str__(self):
        return f"<[{self.word}] [{self.phonetic}] {self.meaning}>"

    @classmethod
    def from_dict(cls, d: dict) -> "Word":
        return cls(
            **d
        )
