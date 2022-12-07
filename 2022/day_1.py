with open('2022/day_1.txt', 'r') as file:
    content = file.read()

elves = content.split('\n\n')
print(max(sum(int(cals) for cals in elf.split('\n')) for elf in elves))

# Part 2
calories = [sum(int(cals) for cals in elf.split('\n')) for elf in elves]
calories.sort(reverse=True)
print(sum(calories[:3]))
