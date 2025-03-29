""".. include:: ../README.md"""  # noqa: D415

from __future__ import annotations

import importlib.metadata

__version__: str
try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

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
    """Convert Japanese Hiragana to Katakana.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The converted text with Hiragana replaced by Katakana.
    """
    for k, v in TRANS_DIC.items():
        text = text.replace(k, v)
    return text


def dewiredify(text: str) -> str:
    """Convert Japanese Katakana to Hiragana.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The converted text with Katakana replaced by Hiragana.
    """
    inverted_dic = {v: k for (k, v) in TRANS_DIC.items()}
    for k, v in inverted_dic.items():
        text = text.replace(k, v)
    return text


__all__ = (
    "__version__",
    "dewiredify",
    "wiredify",
)
