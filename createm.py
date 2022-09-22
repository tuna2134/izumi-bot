import json
import random


with open("model.json") as f:
    model = json.load(f)

last = random.choice(list(model))
message = [last]

while True:
    if last == "。":
        break
    last = random.choice(model[last])
    message.append(last)

print(last)
