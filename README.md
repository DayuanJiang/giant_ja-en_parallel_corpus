# Giant_ja-en_parallel_corpus: 2.8M Ja/En Subtitle Corpus 

This directory includes a giant Japanese-English subtitle corpus. The raw data comes from the Stanford’s [JESC](https://nlp.stanford.edu/projects/jesc/) project.

## Data Example

```
# test.ja
外れ た 音 という もの を 。
私 は 間違っ た 方向 に 偏っ て いる と 思い ます 。
えっ ?、 ギャラ の 支払い 、 待っ て くれ って 。
出会い系 、 援 交 ?
こっち は ニガー の 仕事 だ 。
```

```
# test.en
so it's hard to even describe.
but i think he concentrated on the wrong things.
the kasu high you're telling me is worthless.
these dating sites, sugar sites?
my nigga 's my job.
```

## Contents

- A large corpus consisting of 2.8 million sentences.
- Translations of casual language, colloquialisms, expository writing, and narrative discourse. These are domains that are hard to find in JA-EN MT.

## Modifications

Several pre-processing has been done to make the dataset easier to use.

Overall:

- Delete the pair that Japanese phrase only have only one word.
- The data has been split into train/dev/test set with following size
  - train: 2,795,067 phrase pairs
  - dev: 2,800 phrase pairs
  - test: 2,800 phrase pairs

For English text:

- Add ‘.’ to the end of English phrase if it do not end with punctuation.

For Japanese text:

- Add ‘。’ to the end of Japanese phrase if it do not end with punctuation.
- Replace space inside the phrase with ‘、’.
- Tokenize Japanese with tokenizer `Mecab` and dictionary `mecab-ipadic-neologd`.

