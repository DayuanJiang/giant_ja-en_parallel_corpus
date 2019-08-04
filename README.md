# Giant_ja-en_parallel_corpus: 2.8M Ja/En Subtitle Corpus 

This directory includes a giant Japanese-English subtitle corpus. The raw data comes from the Stanford’s [JESC](https://nlp.stanford.edu/projects/jesc/) project.

## Data Example

```
# test.ja
顔面 パンチ かい ?
お姉ちゃん 、 何で ?
もしくは 実際 の 私 の 要求 を 満たす こと も かのう でしょ う 。
分かっ た 、 リジー 。
夫 を 自分 で 、 けがす こと に なり ます 。
あの 、 それ くらい に 、 し て おい て くれ ない ?
お 掛け 下さい 。
```

```
# test.en
so face punch , huh ?
lisa , no !
or you could actually meet my need .
me ! ok , lizzy .
my husband would defile himself .
hey , can you leave it at that ?
we can sit in here .
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
- Tokenize text with `nltk.

For Japanese text:

- Add ‘。’ to the end of Japanese phrase if it do not end with punctuation.
- Replace space inside the phrase with ‘、’.
- Tokenize text with tokenizer `Mecab` and dictionary `mecab-ipadic-neologd`.

