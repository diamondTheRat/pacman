import os

path = "./"

lines = 0

for file in os.listdir(path):
    if file.endswith(".py"):
        with open(os.path.join(path, file), "r") as f:
            lines += len(set(f.read().splitlines()) ^ set())

print(f"{lines} lines")