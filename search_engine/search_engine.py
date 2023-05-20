import re


def search(docs, query):
    result = []
    query_term = re.findall(r'\w+', query)[0]

    for doc in docs:
        all_terms = re.findall(r'\w+', doc['text'])
        if query_term in all_terms:
            relevance = all_terms.count(query_term)
            result.append({'id': doc['id'], 'relevance': relevance})

    sorted_result = sorted(result, key=lambda i: i['relevance'], reverse=True)
    return [item['id'] for item in sorted_result]
