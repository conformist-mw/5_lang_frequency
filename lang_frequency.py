import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    d = Counter(re.findall(r'[\w]+', text))
    for i in d.most_common(10):
        print(i[0])


if __name__ == '__main__':
    file = load_data(sys.argv[1])
    get_most_frequent_words(file)
