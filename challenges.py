# def get_last_char():
#     answer = input('Enter a word')
#     return answer[-1]
#
# print(get_last_char())


def repeater(phrase, how_many):
    answer = ''
    for x in range (how_many):
        answer += phrase
        print(phrase)
    return answer



repeater('hey', 5)
print(repeater('wow', 10))
