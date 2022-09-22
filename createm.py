import json
import random


with open("model.json") as f:
    model = json.load(f)

print(random.choice(model))
