# wiredify

[![PyPI version](
  <https://badge.fury.io/py/wiredify.svg>
  )](
  <https://badge.fury.io/py/wiredify>
) [![Maintainability](
  <https://qlty.sh/badges/6e8b0efe-da67-4184-adfc-81106a08887a/maintainability.svg>
  )](
  <https://qlty.sh/gh/eggplants/projects/wiredify>
) [![pre-commit.ci status](
  <https://results.pre-commit.ci/badge/github/eggplants/wiredify/master.svg>
  )](
  <https://results.pre-commit.ci/latest/github/eggplants/wiredify/master>
) [![Test Coverage](
  <https://api.codeclimate.com/v1/badges/af70c14ac330cd2c86dc/test_coverage>
  )](
  <https://codeclimate.com/github/eggplants/wiredify/test_coverage>
) [![Code Coverage](
  <https://qlty.sh/badges/6e8b0efe-da67-4184-adfc-81106a08887a/test_coverage.svg>
  )](
  <https://qlty.sh/gh/eggplants/projects/wiredify>
)

[![ghcr latest](
  <https://ghcr-badge.egpl.dev/eggplants/wiredify/latest_tag?trim=major&label=latest>
 ) ![ghcr size](
  <https://ghcr-badge.egpl.dev/eggplants/wiredify/size>
)](
  <https://github.com/eggplants/wiredify/pkgs/container/wiredify>
)

Convert japanese kana from ba-bi-bu-be-bo into va-vi-vu-ve-vo.

## Install

```bash
pip install wiredify
```

## CLI

### Usage

```shellsession
$ wiredify <<< 'ジェネレーティブ・エーアイ'
ジェネレーティヴ・エーアイ

$ wiredify 'ジェネレーティブ・エーアイ'
ジェネレーティヴ・エーアイ

$ echo 'ジェネレーティブ・エーアイ' | wiredify
ジェネレーティヴ・エーアイ

$ wiredify
>>> ジェネレーティブ・エーアイ
ジェネレーティヴ・エーアイ
>>> ...[Press ctrl+d to exit]
$
```

### Help

```shellsession
$ wiredify -h
usage: wiredify [-h] [--invert] [-V] [text]

Convert japanese kana from ba-bi-bu-be-bo into va-vi-vu-ve-vo.

positional arguments:
  text           target text (default: None)

optional arguments:
  -h, --help     show this help message and exit
  --invert       enable dewiredify mode (default: False)
  -V, --version  show program's version number and exit

examples:
  $ wiredify <<< 'ジェネレーティブ・エーアイ'
  ジェネレーティヴ・エーアイ

  $ wiredify 'ジェネレーティブ・エーアイ'
  ジェネレーティヴ・エーアイ

  $ echo 'ジェネレーティブ・エーアイ' | wiredify
  ジェネレーティヴ・エーアイ

  $ wiredify
  >>> ジェネレーティブ・エーアイ
  ジェネレーティヴ・エーアイ
  >>> ...[Press ctrl+d to exit]
  $
```

## Library

### Overview

```python
from wiredify import wiredify
wiredfied_text = wiredify("ジェネレーティヴ・エーアイ")
#=> "ジェネレーティブ・エーアイ"
```

## Other implementations

- Go: [eniehask/wiredify](https://github.com/eniehack/wiredify)
- Rust: [oageo/wiredify](https://github.com/oageo/wiredify)

## License

MIT
