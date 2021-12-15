def part1() -> int:
    with open("input", "r") as f:
        lines = [int(line.strip()) for line in f.readlines()]
        count = 0
        while len(lines) > 1:
            if lines.pop(0) < lines[0]:
                count += 1
    print(count)

def part2() -> int:
    with open("input", "r") as f:
        lines = [int(line.strip()) for line in f.readlines()]
        sums = zip(lines[:-2], lines[1:-1], lines[2:])
        list_of_sums = [sum(numbers) for numbers in list(sums)]
        count = 0
        while len(list_of_sums) > 1:
            popped = list_of_sums.pop(0)
            if popped < list_of_sums[0]:
                count += 1
        print(count)

if __name__ == "__main__":
    part1()
    part2()
