from janome.tokenizer import Tokenizer


text = "なんか僕よりも彼氏みたい。".replace(" ", "")
model = {}
last = ""

t = Tokenizer()
for token in t.tokenize(text):
    message = str(token).split()[0]
    if message == "":
        continue
    if message in model:
        model[last].append(message)
    else:
        model[last] = [message]
    last = message
print(model)
