from janome.tokenizer import Tokenizer


model = {}
last = None

t = Tokenizer()
for token in t.tokenize("マイクラしたい。"):
    if last is None:
        continue
    message = str(token).split()[0]
    if message in model:
        model[last].append(message)
    else:
        model[last] = [message]
    last = message
print(model)
