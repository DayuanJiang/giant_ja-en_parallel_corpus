import re
import random
import MeCab
from tqdm import tqdm
from nltk.tokenize import word_tokenize

random.seed(999)
# https://note.nkmk.me/python-re-regex-character-type/
punctuation_pattern = re.compile('[^\u3041-\u309F|\u30A1-\u30FF|\u4E00-\u9FFF|a-z|A-Z|0-9]')
space_pattern = re.compile(' +')


def add_punctuation(sentence, lang):
    last_token = sentence[-1]
    if lang == "en":
        if last_token.isalpha():
            sentence += "."
    if lang == "ja":
        if not punctuation_pattern.findall(last_token):
            sentence += "。"
        sentence = space_pattern.sub('、', sentence)
    return sentence


def save(dataset, typ):
    en, ja = zip(*dataset)
    with open(typ + ".en", "w", encoding="utf-8") as f:
        f.write("\n".join(en))
    with open(typ + ".ja", "w", encoding="utf-8") as f:
        f.write("\n".join(ja))


def split_dataset(dataset):
    random.shuffle(dataset)
    dev_length = len(dataset) // 1000
    dev_set = dataset[:dev_length]
    test_set = dataset[dev_length:dev_length * 2]
    train_set = dataset[dev_length * 2:]
    return train_set, dev_set, test_set


# read data
en_movie = []
ja_movie = []
with open("raw", "r", encoding="utf-8") as f:
    for line in tqdm(f.readlines()):
        en_sent, ja_sent = line.strip().split("\t")
        if len(ja_sent) > 1:
            en_movie.append(add_punctuation(en_sent, "en"))
            ja_movie.append(add_punctuation(ja_sent, "ja"))

parser = MeCab.Tagger("-O wakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

parsed_ja_movie = []
for sent in tqdm(ja_movie):
    parsed_ja_movie.append(" ".join(parser.parse(sent).split()))

parsed_en_movie = []
for sent in tqdm(en_movie):
    parsed_en_movie.append(" ".join(word_tokenize(sent)))

data = list(zip(parsed_en_movie, parsed_ja_movie))

train_set, dev_set, test_set = split_dataset(data)
save(dev_set, "dev")
save(test_set, "test")
save(train_set, "train")


