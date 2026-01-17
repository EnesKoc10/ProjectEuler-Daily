import math


def is_triangle_number(n):
    if n < 0:
        return False
    x = 8 * n + 1
    root = int(math.isqrt(x))
    return root * root == x


def solve():
    try:
        with open('0042_words.txt', 'r') as file:
            content = file.read()

        words = content.replace('"', '').split(',')
        triangle_word_count = 0

        for word in words:
            word_value = sum(ord(char) - ord('A') + 1 for char in word.upper())

            if is_triangle_number(word_value):
                triangle_word_count += 1

        print(triangle_word_count)

    except FileNotFoundError:
        print("Error: 0042_words.txt not found.")


if __name__ == "__main__":
    solve()
    # 162