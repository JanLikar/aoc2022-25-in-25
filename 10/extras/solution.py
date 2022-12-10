def tick(cycle, x, signals):
    if(cycle % 40 in (x, x+1, x+2)):
        print("#", end="")
    else:
        print(".", end="")

    if(cycle % 40 == 0):
        print()

    if ((cycle - 20) % 40) == 0:
        if cycle not in signals:
            signals[cycle] = (cycle * x)

signals = {}
x = 1
cycle = 0

for line in open("input.txt"):
    match line.split():
        case ["noop"]:
            cycle += 1
            tick(cycle, x, signals)
        case ["addx", n]:
            cycle += 1
            tick(cycle, x, signals)
            cycle += 1
            tick(cycle, x, signals)
            x += int(n)


print(sum(signals.values()))