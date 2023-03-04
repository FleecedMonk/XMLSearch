import argparse
import os
import xml.etree.ElementTree as ET

def search_xml(xml_file, tag, output_file=None, list_tags=False):
    try:
        tree = ET.parse(xml_file, parser=ET.XMLParser(target=ET.TreeBuilder(insert_comments=True), resolve_entities=False))
        root = tree.getroot()
        lines = []
        if list_tags:
            tag_set = set()
            for elem in root.iter():
                tag_set.add(elem.tag)
            print(f"Number of unique tags: {len(tag_set)}")
            for t in tag_set:
                print(t)
        else:
            for child in root.iter(tag):
                line_number = child.sourceline
                line = ET.tostring(child, encoding='unicode')
                lines.append(f"Line {line_number}: {line}")
            output = '\n'.join(lines)
            if output_file:
                with open(output_file, 'w') as f:
                    f.write(output)
            else:
                print(output)
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search an XML document for a tag and display the lines of text that have the tag including the line number from the text.')
    parser.add_argument('xml_file', help='the path to the XML file')
    parser.add_argument('tag', help='the tag to search for')
    parser.add_argument('-o', '--output', help='the path to the output file')
    parser.add_argument('-l', '--list', action='store_true', help='list all unique tags in the document')
    args = parser.parse_args()

    xml_file = args.xml_file
    tag = args.tag
    output_file = args.output
    list_tags = args.list

    if not os.path.isfile(xml_file):
        print(f"Error: {xml_file} is not a valid file path.")
    else:
        search_xml(xml_file, tag, output_file=output_file, list_tags=list_tags)
