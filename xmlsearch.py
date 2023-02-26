import xml.etree.ElementTree as ET

def search_xml_file():
    try:
        # Ask user for search term and file path
        search_term = input("Enter search term (XML tag or text phrase): ")
        file_path = input("Enter path to XML file: ")

        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Search for matching tags or text phrases
        matching_lines = []
        for elem in root.iter():
            if elem.tag == search_term or elem.text == search_term:
                matching_lines.append(ET.tostring(elem, encoding='unicode'))

        # Display matching lines
        print(f"{len(matching_lines)} lines matched the search term '{search_term}':")
        for line in matching_lines:
            print(line)

        # Ask user if they want to save the results to a file
        save_result = input("Do you want to save the results to a file? (YES/NO): ")
        if save_result.upper() == "YES":
            # Ask user for file name and write results to file
            file_name = input("Enter file name to save results: ")
            with open(file_name, "w") as f:
                f.write("\n".join(matching_lines))
                print(f"Results saved to {file_name}")

        # Ask user if they want to search again
        repeat = input("Do you want to perform another search? (YES/NO): ")
        if repeat.upper() == "YES":
            search_xml_file()

    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        search_xml_file()

    except Exception as e:
        print(f"An error occurred: {e}")
        search_xml_file()

# Start the script
search_xml_file()
