import yaml

with open("myst.yml") as f:
    data = yaml.safe_load(f)

for index in range(len(data["project"]["toc"])-1, 0, -1):
    data["project"]["toc"].pop(index)

with open("myst.yml", "w") as f:
    data = yaml.safe_dump(data, f)