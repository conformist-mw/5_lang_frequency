import re
from collections import Counter
import argparse


def load_data(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    d = Counter(re.findall(r'[\w]+', text))
    return [w[0] for w in d.most_common(10)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Выводит 10 самых популярных слов в файле')
    parser.add_argument('filepath', help='укажите файл в формате json')
    args = parser.parse_args()
    data = load_data(args.filepath)
    print('10 самый популярныйх слов в порядке убывания:')
    for num, word in enumerate(get_most_frequent_words(data), 1):
        print(num, word)
