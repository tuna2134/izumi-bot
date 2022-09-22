import json
import random


with open("model.json") as f:
    model = json.load(f)

last = random.choice(list(model))
message = [last]

while True:
    last = random.choice(model[last])
    message.append(last)
    if last in ["。", "！", "？"]:
        break

print("".join(m for m in message))
