import re
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    d = Counter(re.findall(r'[\w]+', text))
    return [w[0] for w in d.most_common(10)]


if __name__ == '__main__':
    pass
