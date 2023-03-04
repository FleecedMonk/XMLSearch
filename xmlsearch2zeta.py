import xml.etree.ElementTree as ET

def main():
    file_name = input("Enter the name of the XML file: ")
    try:
        tree = ET.parse(file_name)
    except Exception as e:
        print(f"Error: {e}")
        return

    root = tree.getroot()

    print("Do you want to:")
    print("1. List all unique tags")
    print("2. Search for a tag")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        unique_tags = set([elem.tag for elem in root.iter()])
        print(f"Total number of unique tags: {len(unique_tags)}")
        for tag in unique_tags:
            print(f"Tag: {tag}")
            count = len([elem.tag for elem in root.iter(tag)])
            print(f"Count: {count}\n")
        run_again = input("Would you like to run the program again? (y/n): ")
        if run_again.lower() == "y":
            main()
    elif choice == "2":
        tag = input("Enter the name of the tag you are searching for: ")
        lines = []
        for child in root.iter(tag):
            line = ET.tostring(child, encoding='unicode')
            lines.append(line)
        if lines:
            output = '\n'.join(lines)
            print(output)
            file_name = input("Enter a file name to save the output to, or press enter to skip: ")
            if file_name:
                with open(file_name, 'w') as f:
                    f.write(output)
            run_again = input("Would you like to run the program again? (y/n): ")
            if run_again.lower() == 'y':
                main()
        else:
            print(f"No occurrences of tag '{tag}' found in the XML file.")
            run_again = input("Would you like to run the program again? (y/n): ")
            if run_again.lower() == 'y':
                main()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()
