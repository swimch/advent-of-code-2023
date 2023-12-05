almanach = {}
with open('test.txt', 'r') as f:
    for line in f:
        if len(line) > 4 and line[4] == "s":
            seeds = line[7:-1].split(" ")
        elif line[0].isalpha():
            category_name = line[:-1].split(":")[0]
            almanach[category_name] = []
        elif line[0].isdigit():
            almanach[category_name].append(line[:-1].split(" "))


def search_destination(source, category):
    for count, map in enumerate(almanach[category]):
        print(map)
        print(f"The current source is {source}")
        print(f"Map No. {count} in {category} is being checked")
        difference = source - int(almanach[category][count][1])
        print(f"The difference between source and source_start is: {difference}")
        print(f"The source_start is: {int(almanach[category][count][1])}")
        if 0 <= difference <= int(almanach[category][count][2]):
            destination = int(almanach[category][count][0]) + difference
            return destination
    destination = source
    return destination


locations = []
print(f"The almanach looks like this: {almanach}")
for seed in seeds:
    source = int(seed)
    print(f"The seed is: {source}")
    for category in almanach:
        print(f"The current category: {category}")
        source = search_destination(source, category)
    locations.append(source)

print(f"the nearest location is: {min(locations)}")