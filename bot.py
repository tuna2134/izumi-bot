from janome.tokenizer import Tokenizer


with open("data/message.txt") as f:
    texts = [m.replace(" ", "") for m in f.readlines()]
model = {}
last = ""

t = Tokenizer()
for text in texts:
    for token in t.tokenize(text):
        print(model)
        message = str(token).split()[0]
        if last == "":
            last = message
            continue
        if message == "。":
            continue
        if message in model:
            try:
                model[last].append(message)
            except KeyError:
                pass
        else:
            model[last] = [message]
        last = message
print(model)
