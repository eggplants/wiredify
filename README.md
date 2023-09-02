# wiredify

[![PyPI version](
  <https://badge.fury.io/py/wiredify.svg>
  )](
  <https://badge.fury.io/py/wiredify>
) [![Maintainability](
  <https://api.codeclimate.com/v1/badges/af70c14ac330cd2c86dc/maintainability>
  )](
  <https://codeclimate.com/github/eggplants/wiredify/maintainability>
) [![pre-commit.ci status](
  <https://results.pre-commit.ci/badge/github/eggplants/wiredify/master.svg>
  )](
  <https://results.pre-commit.ci/latest/github/eggplants/wiredify/master>
) [![Test Coverage](
  <https://api.codeclimate.com/v1/badges/af70c14ac330cd2c86dc/test_coverage>
  )](
  <https://codeclimate.com/github/eggplants/wiredify/test_coverage>
) [![Test](
  <https://github.com/eggplants/wiredify/actions/workflows/test.yml/badge.svg>
  )](
  <https://github.com/eggplants/wiredify/actions/workflows/test.yml>
)

[![ghcr latest](
  <https://ghcr-badge.deta.dev/eggplants/wiredify/latest_tag?trim=major&label=latest>
 ) ![ghcr size](
  <https://ghcr-badge.deta.dev/eggplants/wiredify/size>
)](
  <https://github.com/eggplants/wiredify/pkgs/container/wiredify>
)

Convert japanese kana from va-vi-vu-ve-vo into ba-bi-bu-be-bo.

## Install

```bash
pip install wiredify
```

## CLI

### Usage

```shellsession
$ wiredify <<< 'ジェネレーティヴ・エーアイ'
ジェネレーティブ・エーアイ

$ wiredify 'ジェネレーティヴ・エーアイ'
ジェネレーティブ・エーアイ

$ echo ジェネレーティヴ・エーアイ | wiredify
ジェネレーティブ・エーアイ

$ wiredify
>>> ジェネレーティヴ・エーアイ
ジェネレーティヴ・エーアイ
>>> ...[Press ctrl+d to exit]
$
```

### Help

```shellsession
wiredify -h
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
