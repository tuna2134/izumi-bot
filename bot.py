from janome.tokenizer import Tokenizer


with open("data/message.txt") as f:
    texts = [m.replace(" ", "") for m in f.readlines()]
model = {}
last = ""

t = Tokenizer()
for text in texts:
    for token in t.tokenize(text):
        message = str(token).split()[0]
        if last == "":
            last = message
            continue
        if message == "。":
            continue
        if message in model:
            model[last].append(message)
        else:
            model[last] = [message]
        last = message
print(model)
