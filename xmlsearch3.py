import xml.etree.ElementTree as ET

# Ask for the XML file
xml_file = input("Enter the name of the XML file: ")

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Create dictionaries to store unique tags and attributes
unique_tags = {}
unique_attrs = {}

# Iterate over all elements in the XML file
for elem in root.iter():
    # Count unique tags
    if elem.tag not in unique_tags:
        unique_tags[elem.tag] = 1
    else:
        unique_tags[elem.tag] += 1
    # Count unique attributes
    for attr in elem.attrib:
        if attr not in unique_attrs:
            unique_attrs[attr] = 1
        else:
            unique_attrs[attr] += 1

# Ask the user which task to perform
while True:
    task = input("Enter the task you want to perform (1: list unique tags and attributes, 2: search for a specific attribute): ")
    if task == '1':
        # List unique tags and attributes
        print("Unique tags:")
        for tag, count in unique_tags.items():
            print(f"{tag} ({count} occurrences)")
        print(f"Total unique tags: {len(unique_tags)}")
        print("Unique attributes:")
        for attr, count in unique_attrs.items():
            print(f"{attr} ({count} occurrences)")
        print(f"Total unique attributes: {len(unique_attrs)}")
        # Ask the user if they want to save the output
        save = input("Do you want to save the output? (y/n): ")
        if save.lower() == 'y':
            filename = input("Enter the file name: ")
            with open(filename, 'w') as f:
                f.write("Unique tags:\n")
                for tag, count in unique_tags.items():
                    f.write(f"{tag} ({count} occurrences)\n")
                f.write(f"Total unique tags: {len(unique_tags)}\n")
                f.write("Unique attributes:\n")
                for attr, count in unique_attrs.items():
                    f.write(f"{attr} ({count} occurrences)\n")
                f.write(f"Total unique attributes: {len(unique_attrs)}\n")
        break
    elif task == '2':
        # Search for a specific attribute
        search_field = input("Enter the search field (tag/attribute): ")
        if search_field.lower() == 'tag':
            options = list(unique_tags.keys())
        elif search_field.lower() == 'attribute':
            options = list(unique_attrs.keys())
        else:
            print("Invalid search field.")
            continue
        # Display options and ask for user input
        print("Select an option:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        while True:
            choice = input("Enter the number of the option you want to search for: ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
                print("Invalid choice.")
                continue
            break
        # Search for the chosen option and print output
        search_term = options[int(choice)-1]
        print(f"Lines containing {search_field} '{search_term}':")
        for elem in root.iter():
            if search_field.lower() == 'tag' and elem.tag == search_term:
                print(ET.tostring(elem, encoding='unicode'))
            elif search_field.lower() == 'attribute'
