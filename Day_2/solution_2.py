"""
Description:
Part 2

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

Link to the problem -> https://adventofcode.com/2022/day/2
"""

my_points = 0
second_combo_a = {"Y": 4, "X": 3, "Z": 8}
second_combo_b = {"Y": 5, "X": 1, "Z": 9}
second_combo_c = {"Y": 6, "X": 2, "Z": 7}

file = open("input.txt", 'r')


def part_two(my_points, opponent, me):
    current_points = 0

    if opponent == 'A':
        current_points += second_combo_a[me]
    elif opponent == 'B':
        current_points += second_combo_b[me]
    elif opponent == 'C':
        current_points += second_combo_c[me]

    my_points += current_points
    return my_points


def read_two(my_points):
    while True:
        line = file.readline().split()
        if not line:
            break

        opponent, me = line[0], line[-1]
        match = part_two(my_points, opponent, me)
        my_points = match

    return my_points


print(read_two(my_points))
