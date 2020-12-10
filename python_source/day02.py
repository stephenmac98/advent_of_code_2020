from support import get_input_file

def main():
    # Get the lines of the file
    lines = get_input_file.ReadLines(False)

    ##### Part 1 #####
    print("\nDay 02 Part 1:\n")
    # Track how many properly formatted passwords there are
    count = 0
    for line in lines:
        # Divide the line into it's core components
        line_vals = line.split()

        # Separate out the upper and lower bound
        bounds = line_vals[0].split("-")
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])

        # Find the character to be checked for
        check_char = line_vals[1][:1]

        # Find out how many times the check_char occurred in the string
        value = line_vals[2].count(check_char)

        # Check if the password is valid
        if (value <= upper_bound and value >= lower_bound):
            count = count + 1
    print("There were a total of " + str(count) + " valid passwords")

    ##### Part 2 #####
    print("\nDay 02 Part 2:\n")

    count = 0
    for line in lines:
        # Divide the line into it's core components
        line_vals = line.split()

        # Separate out the upper and lower coords
        coords = line_vals[0].split("-")
        lower_coord = int(coords[0]) - 1
        upper_coord = int(coords[1]) - 1

        # Find the character to be checked for
        check_char = line_vals[1][:1]

        # Check if the password is valid
        if(len(line_vals[2]) < upper_coord):
            continue
        if ((line_vals[2][lower_coord] == check_char) ^ (line_vals[2][upper_coord] == check_char )):
            count = count + 1
    print("There were a total of " + str(count) + " valid passwords")


if __name__ == "__main__":
    main()
