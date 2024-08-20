
import chardet

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

filename = 'leetcode-Question-Scrapper/index_cc.txt'
my_encoding = find_encoding(filename)
with open(filename, 'r', encoding=my_encoding) as f:
    lines = f.readlines()

documents = []
vocab = {}
def preprocess(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[:]]
    return terms


def preprocess_cf(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms
for index, line in enumerate(lines):
    # read statement and add it to the line and then preprocess
    tokens = preprocess(line)
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

filename = 'leetcode-Question-Scrapper/index_cf.txt'
my_encoding = find_encoding(filename)

with open(filename, 'r', encoding=my_encoding) as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    # read statement and add it to the line and then preprocess
    tokens = preprocess_cf(line)
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

filename = 'leetcode-Question-Scrapper/index.txt'
my_encoding = find_encoding(filename)

with open(filename, 'r', encoding=my_encoding) as f:
    lines = f.readlines()

def preprocess_cf(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

for index, line in enumerate(lines):
    # read statement and add it to the line and then preprocess
    tokens = preprocess_cf(line)
    documents.append(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

with open('tf-idf-final/vocab.txt', 'w',encoding='utf-8') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

with open('tf-idf-final/idf-values.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

with open('tf-idf-final/documents.txt', 'w',encoding='utf-8') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))
inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

with open('tf-idf-final/inverted-index.txt', 'w',encoding='utf-8') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))

filename = 'leetcode-Question-Scrapper/Qindex_cc.txt'
links_all = []
with open(filename, 'r', encoding=my_encoding) as f:
    links = (f.readlines())
for link in links:
    links_all.append(link)
filename = 'leetcode-Question-Scrapper/Qindex_cf.txt'
with open(filename, 'r', encoding=my_encoding) as f:
    links = f.readlines()
for link in links:
    links_all.append(link)
filename = 'leetcode-Question-Scrapper/Qindex.txt'
with open(filename, 'r', encoding=my_encoding) as f:
    links = f.readlines()
for link in links:
    links_all.append(link)
with open('tf-idf-final/links.txt', 'w',encoding='utf-8') as f:
    for link in links_all:
        f.write("%s" % link)