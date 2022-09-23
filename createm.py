import json
import random


with open("model.json") as f:
    model = json.load(f)

last = random.choice(model["__BEGIN__"])
begin = "__BEGIN__"
message = [last]

while True:
    last = random.choice(model[last])
    model[last].remove(begin)
    message.append(last)
    begin = last
    if last in ["。", "！", "？"]:
        break

print("".join(m for m in message))
