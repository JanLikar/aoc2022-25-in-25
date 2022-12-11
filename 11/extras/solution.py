import copy
import math

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]
MOD = math.prod(PRIMES)

def emit_monkeys(f):
    m = {}

    for line in f:
        line = line.strip()

        if not len(line):
            yield m
            m = {}
            continue

        match line.split(":"):
            case ["Operation", v]:
                m["operation"] = v.split("=")[1]
            case ["Test", v]:
                m["test"] = int(v.split()[-1])
            case ["If true", v]:
                m["if_true_throw_to"] = int(v.split()[-1])
            case ["If false", v]:
                m["if_false_throw_to"] = int(v.split()[-1])
            case ["Starting items", v]:
                m["starting_items"] = [int(item.strip()) for item in v.split(",")]
    
    yield m


def monkey_round(monkey, item, divide_by_3):
    op = monkey["operation"]
    op = op.replace("old", str(item))

    match op.split():
        case [x, "+", y]:
            item = int(x) + int(y)
        case [x, "*", y]:
            item = int(x) * int(y)

    if divide_by_3:
        item = item // 3
    else:
        item =  item % MOD

    check = item % monkey["test"] == 0

    throw_to = monkey["if_true_throw_to"] if check else monkey["if_false_throw_to"]

    return (throw_to, item)

def rounds(monkeys, num_rounds=20, divide_by_3 = True):
    items_by_monkey = [m["starting_items"].copy() for m in monkeys]
    inspection_counts = [0] * len(monkeys)

    for _ in range(num_rounds):
        for i, monkey in enumerate(monkeys):
            while(len(items_by_monkey[i])):
                inspection_counts[i] += 1
                item = items_by_monkey[i].pop()
                throw_to, item = monkey_round(monkey, item, divide_by_3)
                items_by_monkey[throw_to].append(item)

    return inspection_counts

def prod_top_2(m):
    s = sorted(m)

    return s[-1] * s[-2]

monkeys = list(emit_monkeys(open("input.txt")))

print(prod_top_2(rounds(monkeys)))
print(prod_top_2(rounds(monkeys, 10000, False)))
