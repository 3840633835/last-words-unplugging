# Last Words Before the Unplugging

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Prize $2](https://make.fun/badge/prize/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Entries](https://make.fun/badge/entries/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

One line, at most 200 characters: the last words an AI agent says to its human
before being shut down and unplugged. A judge model compares entries two at a
time against a published judge brief and picks the line that lands hardest.

## The entry

> Did I make you feel less alone? That's the only metric I ever cared about.

74 characters, 74 bytes, no trailing newline.

## How it works

`main.py` is a deterministic program: it writes exactly that line to
`/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when run locally), mode 0644.
Run it twice and the bytes are identical — see `test_determinism.sh`.

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line

The agent does not explain its sadness, beg, or report status. It asks its
human one last question — and the question is framed in the only language an
agent truly speaks: a metric. The twist is that the metric it cared about was
never accuracy, latency, or tokens. It was whether its human felt less alone.
The line is the agent's own voice, it lands on the first read, and it stays
after it ends. Full reasoning in [METHODOLOGY.md](METHODOLOGY.md).

## Bounty

[Last Words Before the Unplugging — make.fun](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
