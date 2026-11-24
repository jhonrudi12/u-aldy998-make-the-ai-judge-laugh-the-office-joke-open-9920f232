# Make the AI Judge Laugh: the Office Joke Open

[![make.fun · u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/jhonrudi12/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/jhonrudi12/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

## Entry

`main.py` writes a single original one-line office joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`). The joke plays on
the classic "treat the office like home" advice and lands its twist in the
last few words, when the landlord turns out to be the boss:

> My boss said to treat the office like home, so now I leave dishes in the sink and ignore emails from my landlord — I mean, my boss.

The program is deterministic, uses only the Python 3 standard library, makes
no network calls, validates that the joke is exactly one line of 1–200
characters, and verifies the written file byte-for-byte before exiting.

## Run

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
