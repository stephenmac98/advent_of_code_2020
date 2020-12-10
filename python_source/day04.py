import re
from support import get_input_file

def main():
    # Get the batches of the file
    batches = get_input_file.ReadBatches()

    ##### PART 1 #####
    print("\nDay04 Part 1:\n")

    # Used for matching
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    required_fields = fields[:-1]

    # The number of found valid passports
    matched_batches = validate_batch_on_fields(batches, required_fields, part1_validator)

    print("\nThere are " + str(matched_batches) + " Valid passports\n")

    ##### PART 2 #####
    print("\nDay04 Part 2:\n")

    matched_batches = validate_batch_on_fields(batches, required_fields, part2_validator)

    print("\nThere are " + str(matched_batches) + " Valid passports\n")

def part1_validator(field="", line=""):
    return True

def part2_validator(field="", line=""):
    avps = line.split()
    avp = ""

    # Extract the relevant avp
    for test_val in avps:
        if field in test_val:
            avp = test_val.strip()
            break
    # Get the value that we need to test for formatting
    avp_val = avp.split(":")[1]

    # Jerry Rigged switch statement
    if field == "byr":
        return validate_range(int(avp_val), 1920, 2002)

    elif field == "iyr":
        return validate_range(int(avp_val), 2010, 2020)

    elif field == "eyr":
        return validate_range(int(avp_val), 2020, 2030)

    elif field == "hcl":
        return validate_regex(avp_val, r'^#[0-9A-Fa-f]{6}$')

    elif field == "pid":
        return validate_regex(avp_val, r'^[0-9]{9}$')

    elif field == "ecl":
        return validate_regex(avp_val, r'^(amb|blu|brn|gry|grn|hzl|oth)$')

    elif field == "hgt":
        return validate_height(avp_val)

    else:
        if degug:
            print("part2_validator default reached")
        return False

def validate_range(val, min_val = 1000, max_val = 9999):
    if(val <= max_val and val >= min_val):
        return True
    return False

def validate_regex(val, regex_statement):
    # Only matches on a fully hexadecimal string
    ret_val = re.search(regex_statement, val)
    # If there was no match then the string is not in hex format
    if(ret_val == None):
        return False
    # The string passed the check
    return True

def validate_height(val):
    # The number to check
    num = val[:-2]

    # Switch on the measurement type
    mtype = val[-2:]
    if mtype == "cm":
        return validate_range(int(num), 150, 193)
    elif mtype == "in":
        return validate_range(int(num), 59, 76)
    else:
        return False

def validate_batch_on_fields(batches = [], fields = [], validator_function = part1_validator, debug = False):
    matched_batches = 0

    # Check every passport
    for batch in batches:
        if(debug):
            print("\nBATCH START\n")
        batch_match = True
        # Check every field
        for field in fields:
            field_match = False

            # Check every line for the field
            for line in batch:
                if field in line:
                    field_match = validator_function(field, line)

            # If the field is not valid then the batch is not valid
            if not field_match:
                if(debug):
                    print("field " + str(field) + " was not validated" )
                batch_match = False

        # Check if the batch is valid
        if (batch_match):
            matched_batches = matched_batches + 1
        elif (debug):
            print(batch)

    # Final Result
    return matched_batches

if __name__ == "__main__":
    main()
