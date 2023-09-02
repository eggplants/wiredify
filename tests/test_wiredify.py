from __future__ import annotations

import pytest

from wiredify import dewiredify, wiredify
from wiredify.main import __main

TEST_CASES: list[tuple[str, str]] = [
    ("ヴォジョレーヌーヴォ", "ボジョレーヌーボ"),
    ("ゔぁゔぃゔゔぇゔぇゔぉ", "ばびぶべべぼ"),
    ("ジェネレーティヴ・エーアイ", "ジェネレーティブ・エーアイ"),
    ("ゔぉるゔぉ", "ぼるぼ"),
    ("ヴァンダル", "バンダル"),
    ("ヴァーイミーツヴォーイ", "バーイミーツボーイ"),
    ("ヴァンヴェール", "バンベール"),
]


@pytest.mark.parametrize("target", TEST_CASES)
def test_wiredify(target: tuple[str, str]) -> None:
    assert wiredify(target[0]) == target[1]


@pytest.mark.parametrize("target", TEST_CASES)
def test_dewiredify(target: tuple[str, str]) -> None:
    assert dewiredify(target[1]) == target[0]


def test_cli_help(capfd: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as e:
        __main(test=["-h"])
    assert e.value.code == 0
    captured = capfd.readouterr()
    assert "va-vi-vu-ve-vo" in captured.out  # pyre-fixme[16]
    assert "usage:" in captured.out
    assert not captured.err  # pyre-fixme[16]


def test_pos_arg(capfd: pytest.CaptureFixture[str]) -> None:
    __main(test=["ゔぁゔぃゔゔぇゔぉ"])
    captured = capfd.readouterr()
    assert captured.out == "ばびぶべぼ\n"  # pyre-fixme[16]
    assert not captured.err  # pyre-fixme[16]


def test_pos_arg_inv(capfd: pytest.CaptureFixture[str]) -> None:
    __main(test=["ばびぶべぼ", "--invert"])
    captured = capfd.readouterr()
    assert captured.out == "ゔぁゔぃゔゔぇゔぉ\n"  # pyre-fixme[16]
    assert not captured.err  # pyre-fixme[16]


class MockedArgs:
    pass


def test_input(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch) -> None:
    i = ["quit", "ゔぁゔぉ"]
    mocked_args = MockedArgs()
    mocked_args.__dict__["invert"] = None
    mocked_args.__dict__["text"] = None
    monkeypatch.setattr("builtins.input", lambda _: i.pop())
    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda _: mocked_args)
    __main(test=[])
    captured = capfd.readouterr()
    assert captured.out == "ばぼ\nbye.\n"  # pyre-fixme[16]
    assert not captured.err  # pyre-fixme[16]
