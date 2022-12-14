from janome.tokenizer import Tokenizer
import json


with open("data/message.txt") as f:
    texts = [m.replace(" ", "").replace("\n", "") for m in f.readlines()]
model = {}
last = "__BEGIN__"

t = Tokenizer("data/userdic.csv", udic_enc="utf8")
for text in texts:
    for token in t.tokenize(text):
        message = str(token).split()[0]
        if last in ["。", "！", "？"]:
            last = message
            continue
        if last in model:
            if not message in model[last]:
                model[last].append(message)
        else:
            model[last] = [message]
        last = message
    last = "__BEGIN__"
print(model)

with open("model.json", "w") as f:
    json.dump(model, f)
