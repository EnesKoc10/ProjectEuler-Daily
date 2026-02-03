import itertools


def solve():
    with open('0059_cipher.txt', 'r') as f:
        cipher_text = [int(x) for x in f.read().split(',')]

    alphabet = range(ord('a'), ord('z') + 1)

    for key in itertools.product(alphabet, repeat=3):
        decrypted_chars = []
        for i in range(len(cipher_text)):
            decrypted_chars.append(cipher_text[i] ^ key[i % 3])

        plain_text = "".join(map(chr, decrypted_chars))

        if " the " in plain_text and " and " in plain_text:
            ascii_sum = sum(decrypted_chars)
            print(f"Key: {''.join(map(chr, key))}")
            print(f"Sum: {ascii_sum}")
            print(f"Text snippet: {plain_text[:50]}...")
            break


if __name__ == "__main__":
    solve()
    # 129448