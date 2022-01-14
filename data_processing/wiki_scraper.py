import sys
import time

import requests
from gensim.corpora import WikiCorpus


def make_corpus(input_file, output_file):

    """Convert Wikipedia xml dump file to text corpus"""

    output = open(output_file, 'w')
    wiki = WikiCorpus(input_file)

    iteration_num = 0
    for text in wiki.get_texts():
        output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
        iteration_num += 1
        if (iteration_num % 500 == 0):
            print('Processed ' + str(iteration_num) + ' articles')
    output.close()
    print('-' * 50)
    print('Processing complete!')
    print('-' * 50)


def check_corpus(input_file):
    
    """Reads some lines of corpus from text file"""

    while(True):
        for _ in range(50):
            print(input_file.readline())
        user_input = input('>>> Type \'STOP\' to quit or hit Any key for more <<< ')
        if user_input == 'STOP':
            break


def load_corpus(input_file):

    """Loads corpus from text file"""

    print('Loading corpus...')
    time1 = time.time()
    corpus = input_flie.read()
    time2 = time.time()
    total_time = time2 - time1
    print('It took %0.3f seconds to load corpus' %total_time)
    return corpus


if __name__ == '__main__':
    url = 'https://dumps.wikimedia.org/kkwiki/latest/kkwiki-latest-pages-articles.xml.bz2'
    articles = requests.get(url, allow_redirects=True)
    with open('../data/raw_data/kkwiki-latest-pages-articles.xml.bz2', 'wb') as input_file:
        input_file.write(articles.content)

    input_file = '../data/raw_data/kkwiki-latest-pages-articles.xml.bz2'
    output_file = '../data/raw_data/kkwiki-latest-pages-articles.txt'
    make_corpus(input_file, output_file)

