from support import get_input_file

def main():
    # Get the batches of the file
    batches = get_input_file.ReadBatches()

    ##### PART 1 #####
    print("\nDay06 Part 1:\n")

    question_sum = 0
    for batch in batches:
        question_sum = question_sum + get_unique_characters(batch)

    print("The total unique questions are: " + str(question_sum))

    ##### PART 2 #####
    print("\nDay06 Part 2:\n")

    question_sum = 0
    for batch in batches:
        question_sum = question_sum + get_common_characters(batch)

    print("The total common questions are: " + str(question_sum))

# Gets the total number of unique characters in a set of lines
def get_unique_characters(group, debug = False):
    # Debug print
    if debug: print("\nGetting Unique Characters")
    if debug: print(group)

    # Genereate the list of unique characters
    unique_characters = []
    for line in group:
        for char in line:
            if char not in unique_characters and char != "\n":
                unique_characters.append(char)

    if debug: print("UNIQUE CHARACTERS:")
    if debug: print(unique_characters)

    # Return the total number of characters
    return len(unique_characters)

# Gets the total number of characters that occur in every line
def get_common_characters(group, debug = False):
    # Debug print
    if debug: print("\nGetting Common Characters")
    if debug: print(group)

    # Genereate the list of common characters
    first_line = True
    common_characters = {}
    lines = 0
    for line in group:
        lines = lines + 1
        for char in line:
            if char != "\n":
                if first_line:
                    common_characters[char] = 1
                elif char in common_characters.keys():
                    common_characters[char] = common_characters[char] + 1
        first_line = False

    if debug: print("COMMON CHARACTERS:")
    if debug: print(common_characters)

    # Figure out which characters occured on every line
    result = 0
    for x in common_characters.values():
        if x == lines:
            result = result + 1

    if debug: print("Total of " + str(result) + " Common Characters")

    # Return the total number of characters
    return result

if __name__ == "__main__":
    main()
