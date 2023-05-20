import re


def search(docs, query):
    result = []
    query_terms = re.findall(r'\w+', query)

    for doc in docs:
        all_terms = re.findall(r'\w+', doc['text'])
        relevance = {'match': 0, 'count': 0}

        for query_term in query_terms:
            if query_term in all_terms:
                relevance['match'] += 1
                relevance['count'] += all_terms.count(query_term)

        if relevance['match']:
            result.append({'id': doc['id'], 'relevance': relevance})

    sorted_result = sorted(
        result,
        key=lambda i: (i['relevance']['match'], i['relevance']['count']),
        reverse=True)
    return [item['id'] for item in sorted_result]
