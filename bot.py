from janome.tokenizer import Tokenizer


text = "TokenCountFilter を使うと，入力文字列中の単語出現頻度を数えることができます。".replace(" ", "")
model = {}
last = ""

t = Tokenizer()
for token in t.tokenize(text):
    print(token)
    print(model)
    message = str(token).split()[0]
    if message in model:
        print(message)
        model[last].append(message)
    else:
        model[last] = [message]
    last = message
print(model)
