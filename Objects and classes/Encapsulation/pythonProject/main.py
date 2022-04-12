def fill_dictionary(words_count):
    for word in words:
        if not word in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1
    return words_count


def print_histogram(words_count):
    for word in words_count:
        print(f"{word}|", end="")
        print("*" * words_count[word])


words = input().split(", ")
words_count = {}

words_count = fill_dictionary(words_count)
print_histogram(words_count)


# for word in words:
#     if not word in words_count:
#         words_count[word] = 1
#     else:
#         words_count[word] += 1

# for word in words_count:
#     print(f"{word}|", end="")
#     print("*" * words_count[word])
