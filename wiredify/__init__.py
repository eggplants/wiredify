from __future__ import annotations

__version__ = "0.1.0"

TRANS_DIC: dict[str, str] = {
    "バ": "ヴァ",
    "ビ": "ヴィ",
    "ベ": "ヴェ",
    "ボ": "ヴォ",
    "ブ": "ヴ",
    "ば": "ゔぁ",
    "び": "ゔぃ",
    "べ": "ゔぇ",
    "ぼ": "ゔぉ",
    "ぶ": "ゔ",
}


def wiredify(text: str) -> str:
    for k, v in TRANS_DIC.items():
        text = text.replace(k, v)
    return text


def dewiredify(text: str) -> str:
    inverted_dic = {v: k for (k, v) in TRANS_DIC.items()}
    for k, v in inverted_dic.items():
        text = text.replace(k, v)
    return text


__all__ = (
    "__version__",
    "wiredify",
    "dewiredify",
)
