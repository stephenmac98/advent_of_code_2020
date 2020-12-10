from support import get_input_file

def main():
    # Get the lines of the file
    lines = get_input_file.ReadLines(False)

    ##### PART 1 #####
    print("\nDay03 Part 1\n")
    result = find_collisions(lines, 3, 0)

    print("Result: " + str(result))

    ##### PART 2 #####
    print("\nDay03 Part 2\n")
    result = find_collisions(lines, 1, 0) * find_collisions(lines, 3, 0) * find_collisions(lines, 5, 0) * find_collisions(lines, 7, 0) * find_collisions(lines, 1, 2)

    print("Result: " + str(result))


def find_collisions(lines = [], line_step = 3, ver_step = 0):
    # Counter for final answer
    trees_hit = 0

    # Track the current position on the line
    traversal_spot = 0

    # Every lines represents moving down by an index of one
    for line in lines:
        if (ver_step != 0):
            ver_step = ver_step + 1
            if(ver_step % 2 == 0):
                continue

        # Read the position on this line
        if(line[traversal_spot] == "#"):
            trees_hit = trees_hit + 1

        # Move to the next line
        traversal_spot = traversal_spot + line_step

        # Shift the spot back onto it's point in the array
        line_len = len(line) - 1 # For some reason len(line) returns 32 on a 31 char line
        if (traversal_spot >= line_len):
            traversal_spot = traversal_spot - line_len

    # return the solution
    return trees_hit



if __name__ == "__main__":
    main()
