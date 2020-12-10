import argparse

# Generate the parser for the command line inputs
parser = argparse.ArgumentParser(description='Find two numbers who sum to 2020, return their multiple')

# --input will represent the input file for this application
parser.add_argument('--input', dest='infile', help='The file with the source numbers')
parser.add_argument('-i', dest='infile', help='The file with the source numbers')

args = parser.parse_args();

# Make sure than an infile was given
if(not args.infile):
    print("An input file is required")
    exit(1)

# Make sure that the infile can be opened
try:
    file = open(args.infile, 'r')
except(OSError, IOError) as e:
    print("The input file could not be opened")
    exit(1)

print("The input file is set to: " + args.infile)

def ReadLines( convert_to_int = False):
    lines = []

    # Add every line to the array
    if(not convert_to_int):
        for line in file.readlines():
            lines.append(line)
    # Convert the input lines into integers
    else:
        for line in file.readlines():
            lines.append(int(line))

    return lines

def ReadBatches():
    batches = []
    lines = []

    # Read every line
    for line in file.readlines():
        # Empty line indicated the end of a batch
        if(line == "\n"):
            batches.append(lines.copy())
            lines = []
        # Line is part of the current batch
        else:
            lines.append(line)

    return batches

