from support import get_input_file

def main():
    lines = get_input_file.ReadLines()

    ##### PART 1 #####
    print("\nDay05 Part 1:\n")
    max_val = 0
    for line in lines:
        pos = get_position(line[:-4], 127)
        row = get_position(line[-4:], 7, "R", "L")
        # Calculate the ID of this seat
        val = (pos * 8) + row
        # Check if the new ID is the largest one found
        if(val > max_val):
            max_val = val

    print("The highest found ID was: " + str(max_val))

    ##### PART 2 #####
    print("\nDay05 Part 2:\n")
    found_ids = []

    # Build a set of every found seat ID
    for line in lines:
        pos = get_position(line[:-4], 127)
        row = get_position(line[-4:], 7, "R", "L")
        # Calculate the ID of this seat
        val = (pos * 8) + row
        found_ids.append(val)

    found_ids = sorted(found_ids)

    previous_id = 0
    for seat_id in found_ids:
        if (seat_id - previous_id == 2):
            print("The ID of my seat: " + str(seat_id - 1))
        previous_id = seat_id

def get_position(line, count, upper_char = "B", lower_char = "F", debug = False):
    if debug: print("Line2: " + str(line))
    lower_bound = 0
    upper_bound = count

    for pos_char in line:
        rounded_val = int(round((upper_bound - lower_bound) / 2))
        if rounded_val == 0:
                rounded_val = 1
        if pos_char == upper_char:
            if debug: print("Rounding Up: " + str(rounded_val))
            lower_bound = lower_bound + rounded_val
        elif pos_char == lower_char:
            if debug: print("Rounding Down: " + str(rounded_val))
            upper_bound = upper_bound - rounded_val
        else:
            print("Inproper character passed to get_position")
            return -1
        if debug: print("Upper Bound: " + str(upper_bound) + " Lower Bound " + str(lower_bound))
        if lower_bound == upper_bound:
            return lower_bound

    # An error has occured and no character was found
    print("There was no solution found by get_position")
    return -1


if __name__ == "__main__":
    main()
