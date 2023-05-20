import re


def search(docs, query):
    result = []
    query_term = re.findall(r'\w+', query)[0]

    for doc in docs:
        doc_id, text = doc['id'], doc['text']
        all_terms = re.findall(r'\w+', text)
        if query_term in all_terms:
            result.append(doc_id)

    return result
