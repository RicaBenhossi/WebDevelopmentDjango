# def test(x):
#     if x < 3:
#         print("Teste com x em ", x)
#         test(x + 1)

# print(test(0))

def censor(text, word):
    new_phrase = ''
    # text = text.split(' ')
    for (n in text.split(" ")):
        if (n == word):
            new_phrase += 
        else:
            new_phrase += n + ' '
    print(type(new_phrase))
    return new_phrase


print(censor("teste de teste", "A"))