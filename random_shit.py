import os

path = "./"

classes = 0

for file in os.listdir(path):
    if file.endswith(".py"):
        with open(os.path.join(path, file), "r") as f:
            text = f.read().split()
            for word in text:
                if word == "class":
                    classes += 1

print(f"{classes} classes")