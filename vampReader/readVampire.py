counter = 0

with open("dracula.txt", "r") as foo:
    with open("vampytimex.txt", "w") as fang:
        with open("vampytimes.txt", "w") as vampytimes:
            for line in foo:
                if "vampire" in line.lower():
                    print(line)
                    counter += 1
                    fang.write(line)
                    vampytimes.write(line)

print(counter)

