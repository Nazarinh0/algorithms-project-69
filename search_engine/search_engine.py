import re


def search(docs, query):
    result = []
    query_term = re.findall(r'\w+', query)[0]

    for doc in docs:
        all_terms = re.findall(r'\w+', doc['text'])
        if query_term in all_terms:
            result.append(doc['id'])

    return result
