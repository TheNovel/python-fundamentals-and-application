with open("data/step04.txt") as source, open("output/step04.txt", "w") as target:
    l = []
    for line in source:
        l.append(line.strip())
    l.reverse()
    text = "\n".join(l)
    target.write(text)
