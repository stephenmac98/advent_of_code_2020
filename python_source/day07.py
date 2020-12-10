from support import get_input_file

def main():
    lines = get_input_file.ReadLines()

    ##### PART 1 #####
    print("\nDay04 Part 1:\n")

    # Contains every bag in the list
    bags = []

    # Generate the bags array
    for line in lines:
        bags.append(Bag(line))

    res = find_containing_bags_extended(bags, "shiny gold bag", False)
    print("There are " + str(res) + " Bags that can contain a shiny gold bag")

    ##### PART 2 #####
    print("\nDay04 Part 2:\n")

    target_bag = get_bag(bags, "shiny gold bag")

    ret = find_contained_bags(bags, target_bag, False)
    res = []
    while (len(ret) > 0):
        cur = []
        for bag in ret:
            cur.extend(find_contained_bags(bags, bag, False))
        res.extend(ret)
        ret = cur.copy()
        print("There are " + str(len(res)) + " Currently Found")
    print("\nThere are " + str(len(res)) + " Contained bags")

def get_bag(bags, name):
    for bag in bags:
        if bag.name == name:
            return bag
    return None

def print_containing_bags(containing_bags):
    for bag in containing_bags:
        print("---bag---")
        print(bag.name)
        print(bag.restrictions)
        print("\n")

def find_contained_bags(bags, bag, debug = False):
    if debug: print("##### find_contained_bags #####")
    if debug: print("### Bag")
    if debug: print_containing_bags([bag])
    contained_bags = []
    for t_bag in bags:
        if debug: print(t_bag.name)
        if debug: print(t_bag.restrictions)
        if bag.contains(t_bag):
            for i in range(bag.restrictions[t_bag.name]):
                contained_bags.append(t_bag)
    if debug: print("#####ANSWER")
    if debug: print_containing_bags(contained_bags)
    if debug: print("###############################")
    return contained_bags

def find_containing_bags_extended(bags, name, debug = False):
    containing_bags = []
    new_containing_bags = []

    new_containing_bags = find_containing_bags(bags, "shiny gold bag")
    containing_bags = new_containing_bags.copy()

    while(len(new_containing_bags) > 0):
        if debug: print("\n***********************************")
        if debug: print("**********Initial Containing Bags**********")
        if debug: print_containing_bags(containing_bags)
        if debug: print("**********Initial New Containing Bags**********")
        if debug: print_containing_bags(new_containing_bags)
        if debug: print("\n**********Bag Loop**********")

        tmp_containing_bags = []
        for bag in new_containing_bags:
            if debug: print(bag.name)
            tmp_containing_bags.extend(find_containing_bags(bags, bag.name, debug))

        if debug: print("**********Found Containing Bags**********")
        if debug: print_containing_bags(tmp_containing_bags)

        new_containing_bags = test_for_new_items(containing_bags, tmp_containing_bags, debug)
        containing_bags.extend(new_containing_bags)

        if debug: print("**********Final Containing Bags**********")
        if debug: print_containing_bags(containing_bags)
        if debug: print("**********Final New Containing Bags**********")
        if debug: print_containing_bags(new_containing_bags)
        if debug: print("***********************************\n")

    return len(containing_bags)

def test_for_new_items(old, new, debug = False):
    if debug: print("#####TEST FOR NEW ITEMS#####")
    if debug: print("###New Bag")
    if debug: print_containing_bags(old)
    if debug: print("###Old Bag")
    if debug: print_containing_bags(new)
    items = []
    # Find any new items
    for item in new:
        if item not in old and item not in items:
            items.append(item)
    if debug: print("###Unique Bag")
    if debug: print_containing_bags(items)
    if debug: print("############################")
    return items

def find_containing_bags(bags, name, debug = False):
    containing_bags = []
    for bag in bags:
        for restriction in bag.restrictions.keys():
            if restriction == name:
                containing_bags.append(bag)
    return containing_bags

class Bag:
    def __init__(self, line, debug = False):
        components= line.split("contain")
        self.debug = debug

        if self.debug: print("\nBag Initialization called")
        if self.debug: print("COMPONENTS:")
        if self.debug: print(components)
        self.name = components[0][:-2]
        self.restrictions = self.establish_restrictions(components[1])

    def establish_restrictions(self, line):
        restrictions_dict = {}
        restrictions = line.rstrip().replace('.','').split(',')
        if self.debug: print("RESTRICTIONS")
        if self.debug: print(restrictions)
        for restriction in restrictions:
            number = restriction[1:2]
            if number == "n":
                number = 0
                rule = restriction[4:]
            else:
                number = int(number)
                rule = restriction[3:]
            if number > 1:
                rule = rule[:-1]
            if self.debug: print("RULE")
            if self.debug: print(rule)
            restrictions_dict[rule] = number
        if self.debug: print("Generated Bag Restrictions")
        if self.debug: print(str(restrictions_dict))
        # Return the filled dictionary
        return restrictions_dict

    def contains(self, bag):
        for t_bag in self.restrictions.keys():
            if t_bag == bag.name:
                return True
        return False

if __name__ == "__main__":
    main()

