### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nazarinh0/algorithms-project-69/workflows/hexlet-check/badge.svg)](https://github.com/Nazarinh0/algorithms-project-69/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d6535725cdca173cbec1/maintainability)](https://codeclimate.com/github/Nazarinh0/algorithms-project-69/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d6535725cdca173cbec1/test_coverage)](https://codeclimate.com/github/Nazarinh0/algorithms-project-69/test_coverage)

# Search Engine Project
The Internet is hard to imagine without search engines. To make them work effectively, different search engines are used. In this project, we will write our own implementation of a search engine.

A popular open-source search engine is ElasticSearch.

## Usage Example

```from search_engine.search_engine import search

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."

docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
]

result = search(docs, 'shoot')
print(result)  # => ['doc2', 'doc1']
```

This code demonstrates how to use the search function from my search engine module to search for documents containing the word "shoot" in the list of documents represented by Python dictionaries in the docs list. The search function returns a list of document IDs (represented as strings) where the search query was found.
