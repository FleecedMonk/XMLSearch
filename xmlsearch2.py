import xml.etree.ElementTree as ET

while True:
    xml_file = input("Enter the path to the XML file: ")
    try:
        tree = ET.parse(xml_file)
        break
    except:
        print("Error parsing the XML file. Please try again.")

while True:
    xml_tag = input("Enter the XML tag to search for: ")
    root = tree.getroot()
    lines = []
    for i, child in enumerate(root.iter(xml_tag)):
        line = ET.tostring(child, encoding='unicode', method='xml').strip()
        lines.append(f"Line {child.sourceline}: {line}")
    if len(lines) > 0:
        break
    else:
        print("The XML tag was not found. Please try again.")

while True:
    output_file = input("Enter the path to save the output text file: ")
    try:
        with open(output_file, 'w') as f:
            f.write('\n'.join(lines))
        break
    except:
        print("Error saving the output file. Please try again.")

    run_again = input("Do you want to run the program again? (y/n) ")
    if run_again.lower() != 'y':
        break
