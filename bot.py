from janome.tokenizer import Tokenizer


model = {}
last = ""

t = Tokenizer()
for token in t.tokenize("TokenCountFilter を使うと，入力文字列中の単語出現頻度を数えることができます。"):
    print(token)
    print(model)
    message = str(token).split()[0]
    if message in model:
        model[last].append(message)
    else:
        model[last] = [message]
    last = message
print(model)
