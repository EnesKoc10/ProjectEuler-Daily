def solve():
    ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
    hundred = 7
    and_word = 3
    thousand = 11

    total_letters = 0

    for i in range(1, 1001):
        if i == 1000:
            total_letters += thousand
        else:
            h = i // 100
            t = (i // 10) % 10
            o = i % 10

            if h > 0:
                total_letters += ones[h] + hundred
                if t > 0 or o > 0:
                    total_letters += and_word

            if t == 1:
                total_letters += teens[o]
            else:
                total_letters += tens[t] + ones[o]

    return total_letters


print(solve())
# 21124