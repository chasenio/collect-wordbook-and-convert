from typing import Optional
from typing import List
from dataclasses import dataclass
from dataclasses import field
import yaml


@dataclass
class Store:
    words: List["Word"] = field(default_factory=list)

    def add(self, word: "Word"):
        self.words.append(word)

    def __iter__(self):
        return iter(self.words)

    def __len__(self):
        return len(self.words)

    def dump(self, file: str):
        """支持中文"""
        words_dict = [word.__dict__ for word in self.words]
        with open(file, 'w') as f:
            yaml.dump(words_dict, f, allow_unicode=True)


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
