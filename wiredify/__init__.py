from __future__ import annotations

__version__ = "0.0.0"

TRANS_DIC: dict[str, str] = {
    "ヴァ": "バ",
    "ヴィ": "ビ",
    "ヴェ": "ベ",
    "ヴォ": "ボ",
    "ヴ": "ブ",
    "ゔぁ": "ば",
    "ゔぃ": "び",
    "ゔぇ": "べ",
    "ゔぉ": "ぼ",
    "ゔ": "ぶ",
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
