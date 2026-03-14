import math
from collections import defaultdict
from itertools import permutations


def get_word_anagrams():
    with open("0098_words.txt", "r") as f:
        words = f.read().replace('"', '').split(',')

    anagram_groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        anagram_groups[key].append(word)

    pairs = []
    for group in anagram_groups.values():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    pairs.append((group[i], group[j]))
    return pairs


def is_square(n):
    return math.isqrt(n) ** 2 == n


def solve():
    word_pairs = get_word_anagrams()
    max_square = 0

    for w1, w2 in word_pairs:
        unique_chars = "".join(set(w1))
        num_chars = len(unique_chars)

        for p in permutations("0123456789", num_chars):
            mapping = dict(zip(unique_chars, p))

            if mapping[w1[0]] == '0' or mapping[w2[0]] == '0':
                continue

            val1 = int("".join(mapping[c] for c in w1))
            if is_square(val1):
                val2 = int("".join(mapping[c] for c in w2))
                if is_square(val2):
                    max_square = max(max_square, val1, val2)

    return max_square


print(solve())
# 18769