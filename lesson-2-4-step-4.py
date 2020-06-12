with open("text.txt") as f, open("reversed_text.txt", "w") as w:
    text = []
    for line in f:
        text.append(line.strip())
    text.reverse()
    w.write("\n".join(text))
