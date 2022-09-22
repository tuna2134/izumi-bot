from janome.tokenizer import Tokenizer


model = {}
last = ""

t = Tokenizer()
for token in t.tokenize("マイクラしたい。"):
    message = str(token).split()[0]
    if message in model:
        model[message].append(last)
    else:
        model[message] = [last]
    last = message
print(model)
