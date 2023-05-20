from search_engine.search_engine import search


query = "shoot"
query_with_signs = "shoot!"
query_compound = 'shoot straight'

documents = [
    {'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"},
    {'id': 'doc2', 'text': "Just run away and don't look back."},
    {'id': 'doc3', 'text': "Don't shoot shoot shoot that thing at me."},
    {'id': 'doc4', 'text': "I'm your shooter."},
    {'id': 'doc5', 'text': "Please don't shoot! If you shoot I gonna die."}
]

empty_documents = []


def test_query():
    result = search(documents, query)
    assert result == ['doc3', 'doc5', 'doc1']


def test_query_with_signs():
    result = search(documents, query_with_signs)
    assert result == ['doc3', 'doc5', 'doc1']


def test_query_compound():
    result = search(documents, query_compound)
    assert result == ['doc1', 'doc3', 'doc5']


def test_empty_docs():
    result = search(empty_documents, query)
    assert result == []
