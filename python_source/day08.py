from support import get_input_file

def main():
    lines = get_input_file.ReadLines()

    ##### PART 1 #####
    print("\nDay08 Part 1:\n")

    instructions = []
    for line in lines:
        ins = Instruction(line)
        instructions.append(ins)

    res = find_loop(instructions)

    print("The final accumulator is " + str(res[1]))

    ##### PART 2 #####
    print("\nDay08 Part 2:\n")

    res = find_no_loop(instructions)
    print("The final accumulator is " + str(res))

# Run the instructions until a position is reached that has been reached before
def find_loop(instructions):
    game = State_Tracker(instructions)
    reached_positions = []
    pos = 0

    while pos not in reached_positions:
        reached_positions.append(pos)
        pos = game.perform_instruction()
        if pos > len(instructions) - 1:
            print("Solution Found")
            return [1, game.accumulator]

    return [0, game.accumulator]

# Don't even want to imagine the O(f(n)) of this one
# Changes every instruction one at a time and checks if the new instruction set finished without a loop
def find_no_loop(instructions):
    for instruction in instructions:
        if instruction.type in ["jmp", "nop"]:
            instruction.flip()
            res = find_loop(instructions)
            instruction.flip()
            if res[0] == 1:
                return res[1]
    return -1

# Manages the state of the game, including the instructions, accumulator, and line position
class State_Tracker:
    def __init__(self, instructions):
        self.line_position = 0
        self.accumulator = 0
        self.instructions = instructions

    def perform_instruction(self, debug = False):
        instruction = self.instructions[self.line_position]
        if debug:
            print("Instruction: " + str(instruction.type) + " " + str(instruction.value))
        if instruction.type == "nop":
            if debug: print("nop executing")
            self.line_position = self.line_position + 1
        elif instruction.type == "acc":
            if debug: print("acc executing")
            self.line_position = self.line_position + 1
            self.accumulator = self.accumulator + instruction.value
        elif instruction.type == "jmp":
            if debug: print("jmp executing")
            self.line_position = self.line_position + instruction.value
        else:
            print("Invalid instruction type " + instruction.type)
            exit(1)
        return self.line_position

# Stores the type and value of an instruction
class Instruction:
    def __init__(self, line, debug = False):
        vals = line.split()
        self.type = vals[0]
        self.value = int(vals[1])
        if debug:
            print("Instruction Type: " + self.type)
            print("Instruction Val: " + str(self.value))

    def flip(self):
        if self.type == "jmp":
            self.type = "nop"
        elif self.type == "nop":
            self.type = "jmp"
        else:
            print("flip called on invalid type")
            exit(1)

if __name__ == "__main__":
    main()
