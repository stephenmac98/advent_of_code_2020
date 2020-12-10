from support import get_input_file

def main():
    lines = get_input_file.ReadLines(True)

    ##### PART 1 #####
    print("\nDay04 Part 1:\n")

    res = validate_numbers(lines, 25, False)

    print("The first number to fail the encryption scheme is " + str(res))

    ##### PART 2 #####
    print("\nDay04 Part 2:\n")

    res = find_contiguous_set(lines, res)
    print("The index of the set is [" + str(res[0]) + ", " + str(res[1]) + "]")
    val = find_largest_in_set(lines, 1, res[0], res[1])[0] + find_smallest_in_set(lines, 1, res[0], res[1])[0]
    print("The sum of the values at that index is " + str(val))


def find_largest_in_set(numbers, count=1, lower_bound=0, upper_bound= -1):
    if upper_bound < 0:
        upper_bound = len(numbers) -1
    res = []
    for i in range(lower_bound, upper_bound + 1):
        if len(res) < count:
            res.append(numbers[i])
        else:
            m_val = min(res)
            if numbers[i] > m_val:
                res.remove(m_val)
                res.append(numbers[i])
    return res

def find_smallest_in_set(numbers, count=1, lower_bound=0, upper_bound= -1):
    if upper_bound < 0:
        upper_bound = len(numbers) -1
    res = []
    for i in range(lower_bound, upper_bound + 1):
        if len(res) < count:
            res.append(numbers[i])
        else:
            m_val = min(res)
            if numbers[i] < m_val:
                res.remove(m_val)
                res.append(numbers[i])
    return res


def find_contiguous_set(numbers, target_sum):
    lower_bound = 0
    upper_bound = 1
    cur_sum = get_sum_in_subset(numbers, lower_bound, upper_bound)
    while(cur_sum != target_sum):
        if cur_sum > target_sum:
            lower_bound = lower_bound + 1
        else:
            upper_bound = upper_bound + 1

        if lower_bound >= upper_bound or upper_bound > len(numbers):
            print("Find Contiguous Set failed")
            return -1

        cur_sum = get_sum_in_subset(numbers, lower_bound, upper_bound)
    return [lower_bound, upper_bound]


def get_sum_in_subset(numbers, lower, upper):
    sum_val = 0
    for i in range(lower, upper + 1):
        sum_val = sum_val + numbers[i]
    return sum_val


def validate_numbers(lines, depth, debug = False):
    numbers = []
    for line in lines:
        if debug:
            print("Testing for Number: ")
            print(line)
        if len(numbers) < depth:
            numbers.append(line)
        else:
            if( not validate_sum_exists(numbers, line, debug)):
                return line
            else:
                numbers.pop(0)
                numbers.append(line)
    return -1

def validate_sum_exists(numbers, num, debug = False):
    for t_num in numbers:
        for t_num2 in numbers:
            if debug: print("Testing " + str(t_num) + " : " + str(t_num2) + " for " + str(num))
            if t_num + t_num2 == num and t_num != t_num2:
                return True
    return False

if __name__ == "__main__":
    main()

