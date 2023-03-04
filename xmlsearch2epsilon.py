import xml.etree.ElementTree as ET

def list_unique_tags(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        unique_tags = {}
        for child in root.iter():
            if child.tag in unique_tags:
                unique_tags[child.tag] += 1
            else:
                unique_tags[child.tag] = 1
        total_tags = len(unique_tags)
        print(f"Total number of unique tags: {total_tags}")
        for tag, count in unique_tags.items():
            print(f"{tag}: {count}")
    except Exception as e:
        print(f"Error: {e}")

def search_xml(file, tag):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        lines = []
        for child in root.iter(tag):
            line_number = child.sourceline
            line = ET.tostring(child, encoding='unicode')
            lines.append(f"Line {line_number}: {line}")
        output = '\n'.join(lines)
        print(output)
        file_name = input("Enter a file name to save the output to, or press enter to skip: ")
        if file_name:
            with open(file_name, 'w') as f:
                f.write(output)
        run_again = input("Would you like to run the program again? (y/n): ")
        if run_again.lower() == 'y':
            main()
    except Exception as e:
        print(f"Error: {e}")

def main():
    xml_file = input("Enter the path to the XML file: ")
    choice = input("Type 'list' to list all unique tags and their counts or 'search' to search for a specific tag: ")
    if choice == "list":
        list_unique_tags(xml_file)
    elif choice == "search":
        tag = input("Enter the XML tag to search for: ")
        search_xml(xml_file, tag)
    else:
        print("Invalid choice. Please enter 'list' or 'search'.")
        main()

if __name__ == '__main__':
    main()
