from __future__ import annotations

import os

import pytest

from wiredify import __version__, dewiredify, wiredify
from wiredify.main import __main, __repl

TEST_CASES: list[tuple[str, str]] = [
    ("ボジョレーヌーボ", "ヴォジョレーヌーヴォ"),
    ("ばびぶべべぼ", "ゔぁゔぃゔゔぇゔぇゔぉ"),
    ("ジェネレーティブ・エーアイ", "ジェネレーティヴ・エーアイ"),
    ("ぼるぼ", "ゔぉるゔぉ"),
    ("バンダル", "ヴァンダル"),
    ("バーイミーツボーイ", "ヴァーイミーツヴォーイ"),
    ("バンベール", "ヴァンヴェール"),
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
    assert "va-vi-vu-ve-vo" in captured.out
    assert "usage:" in captured.out
    assert not captured.err


def test_cli_version(capfd: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as e:
        __main(test=["-V"])
    assert e.value.code == 0
    captured = capfd.readouterr()
    assert __version__ + "\n" == captured.out
    assert not captured.err


def test_pos_arg(capfd: pytest.CaptureFixture[str]) -> None:
    __main(test=["ばびぶべぼ"])
    captured = capfd.readouterr()
    assert captured.out == "ゔぁゔぃゔゔぇゔぉ\n"
    assert not captured.err


def test_pos_arg_inv(capfd: pytest.CaptureFixture[str]) -> None:
    __main(test=["ゔぁゔぃゔゔぇゔぉ", "--invert"])
    captured = capfd.readouterr()
    assert captured.out == "ばびぶべぼ\n"
    assert not captured.err


class MockedArgs:
    pass


def test_stdin(
    capfd: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mocked_args = MockedArgs()
    mocked_args.__dict__["invert"] = None
    mocked_args.__dict__["text"] = None
    monkeypatch.setattr("sys.stdin.isatty", lambda: False)
    monkeypatch.setattr("sys.stdin.read", lambda: "バボ")
    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda _: mocked_args)
    __main(test=[])
    captured = capfd.readouterr()
    assert captured.out == "ヴァヴォ\n"
    assert not captured.err


def test_repl(
    capfd: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    i = ["quit", "バボ"]
    mocked_args = MockedArgs()
    mocked_args.__dict__["invert"] = None
    mocked_args.__dict__["text"] = None
    monkeypatch.setattr("builtins.input", lambda _: i.pop())
    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda _: mocked_args)
    __main(test=[])
    captured = capfd.readouterr()
    assert captured.out == "ヴァヴォ\nbye.\n"
    assert not captured.err


def test_repl_int(
    capfd: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def mocked_func(_text: str) -> str:
        if "PYTEST_CURRENT_TEST" in os.environ:
            raise KeyboardInterrupt
        return "Never."

    mocked_args = MockedArgs()
    mocked_args.__dict__["invert"] = None
    mocked_args.__dict__["text"] = None
    monkeypatch.setattr("builtins.input", lambda _: "ヴォ")
    __repl(func=mocked_func)
    captured = capfd.readouterr()
    assert captured.out == "bye.\n"
    assert not captured.err
