from janome.tokenizer import Tokenizer
import json


with open("data/message.txt") as f:
    texts = [m.replace(" ", "") for m in f.readlines()]
print(texts)
model = {}
last = ""

t = Tokenizer()
for text in texts:
    for token in t.tokenize(text):
        message = str(token).split()[0]
        if last == "":
            last = message
            continue
        if last in model:
            if not message in model[last]:
                model[last].append(message)
        else:
            model[last] = [message]
        last = message
print(model)

with open("model.json", "w") as f:
    json.dump(model, f)
