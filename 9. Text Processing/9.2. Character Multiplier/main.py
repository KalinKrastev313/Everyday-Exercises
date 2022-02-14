first_word, second_word = input().split()
result = 0

def shorter_word_length (first_word = first_word, second_word = second_word):
    if len(first_word) < len(second_word):
        return len(first_word), second_word
    else:
        return len(second_word), first_word

def multiplication(lenght):
    m_result = 0
    for index in range(lenght):
        m_result += ord(first_word[index])*ord(second_word[index])
    return m_result

def addition(lenght, long_word):
    add_result = 0
    for char in range(lenght, len(long_word)):
        add_result += ord(long_word[char])
    return add_result

length , long_word = shorter_word_length()
result += multiplication(length)
result += addition(length, long_word)
print(result)