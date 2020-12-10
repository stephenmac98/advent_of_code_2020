from support import get_input_file

def main():
    ##### PART 1 #####
    print("\nDay01 Part 1: \n")
    # O(nlog(n)) maybe use radix sort instead
    lines = sorted(get_input_file.ReadLines(True))

    lowIndex = 0
    highIndex = len(lines) - 1
    tot = lines[lowIndex] + lines[highIndex]

    # Super Sexy O(n) Solution
    while (tot != 2020):
        if(tot > 2020):
            highIndex = highIndex - 1
        else:
            lowIndex = lowIndex + 1
        if(lowIndex >= highIndex):
            print("Script failed to find a solution")
            exit(1)
        tot = lines[lowIndex] + lines[highIndex]

    answer = lines[lowIndex] * lines[highIndex]

    print("The two numbers are: " + str(lines[lowIndex]) + " " + str(lines[highIndex]))
    print("The answer is: " + str(answer))

    ##### PART 2 #####
    print("\nDay01 Part 2: \n")
    answer = find_result(lines)
    print("The answer to part 2 is: " + str(answer));

# Super Unsexy O(n^3) intolerably bad
def find_result(lines = []):
    for i in range(len(lines) - 3):
        for j in range(i + 1, len(lines) - 2):
            for k in range(j + 1, len(lines) - 1):
                if(lines[i] + lines[j] + lines[k] == 2020):
                    print("The three numbers are: " + str(lines[i]) + " " + str(lines[j]) + " " + str(lines[k]))
                    return lines[i] * lines[j] * lines[k]

if __name__ == "__main__":
    main()
