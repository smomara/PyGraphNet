from graphent.graph import Graph
from graphent import visualize

def is_one_letter_off(word1, word2):
    if len(word1) != len(word2):
        return False
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

words = [
    "AIM", "ARM", "ARC", "ART", "ACT", "RAT", "OAT", "CAT",
    "OAR", "TAR", "CAR",
]

word_graph = Graph(vertices=words)

for i, word1 in enumerate(words):
    for word2 in words[i+1:]:
        if is_one_letter_off(word1, word2) or is_anagram(word1, word2):
            word_graph.add_edge((word1, word2))

visualize(word_graph, notebook=False, filename="word_graph")