# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/sagaevil530/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/sagaevil530/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world news of **Wednesday 18 November 2026** — a
newspaper front page: the date in the masthead, a lead story on President
Trump's welcome by President Marcos in Manila, and four more stories from
the day: APEC opening in Shenzhen, the US strike on an Iranian missile site
on Qeshm Island, Cyclone Akvan in the Bay of Bengal, and a new speaker
taking the chair in Israel's Knesset.

![The world's news of 18 November 2026](entry.png)

## Stories in the image

- **Manila** — Trump receives full military honours from Marcos Jr. at
  Malacañang, with a state banquet, before flying on to Shenzhen for APEC.
- **Shenzhen** — APEC leaders meet 18–19 November; a Trump–Xi–Putin
  meeting on nuclear arms is set for Thursday.
- **The Gulf** — US forces strike an Iranian missile site on Qeshm Island
  after Iranian drones targeted a US radar in Bahrain; tankers are hit in
  the Strait of Hormuz.
- **Bay of Bengal** — Cyclone Akvan strengthens into a severe cyclonic
  storm; heavy rain reaches India's east coast, with landfall due Friday.
- **Jerusalem** — Matan Kahana, an ally of Gadi Eisenkot, takes over as
  Knesset speaker after a 66–52 vote, a blow to Netanyahu.
- **Also today** — a US House briefing on the Nvidia affair is due.

## How it was made

The three scene illustrations (`assets/`) were generated with no text in
them. The front page — masthead, headlines, captions and the two pictograms
(cyclone, parliament) — was composed with Python/PIL in `compose.py`, so
every label is crisp rendered text. `main.ts` copies the finished
`entry.png` to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/entry.png` is a 1024×1024 PNG of under 1 MiB. Running the program
twice writes byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
