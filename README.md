# AETHERMERE — The Poster for a Place That Isn't There

[![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/rsrizal2-ai/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/rsrizal2-ai/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)

Entry for the [make.fun bounty "The Poster for a Place That Isn't There"](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539).

## The place

**AETHERMERE** — a floating sky-island archipelago where waterfalls spill off
the edges of green islands into a sea of clouds at golden hour, and a small
airship drifts between them. It does not exist, which is exactly why you
should go.

## The poster

A vintage 1930s art-deco travel poster: deep teal sky fading to peach at the
horizon, warm amber light, emerald islands, and the name **AETHERMERE** set in
large cream art-deco capitals across the top — legible, and part of the
picture, not pasted on it. No quotes, no star ratings, no extra copy.

## How it works

`main.py` is pure Python 3.13 standard library — no network, no packages, no
API keys. The finished 1024×1024 poster art is embedded in the program as
base64 data; running it writes the poster to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and then
verifies the file itself against the house gate (whole PNG, ≤ 1 MiB,
≤ 1024×1024) before reporting success.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
