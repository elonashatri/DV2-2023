import glob
from tqdm import tqdm
import os
from xml.dom import minidom
import json

# ALWAYS PUT / IN THE END
XML_DIR = '/homes/es314/xml_and_images_only/polyphonic/xml_by_page/'
XML_PATH = XML_DIR + '*.xml'

EXPORT_FILE = '/homes/es314/DV2-2023/classes_to_files.json'


def main():
    # Get all XML
    available_xml = glob.glob(XML_PATH)
    print('available_xml: ', len(available_xml))

    # For each classname, add the current file if not existing
    # "noteheadBlack": [file1.xml, file2.xml]

    classnames_files = {}
    # Run through all files, then extract classnames
    for xml_file in tqdm(available_xml, desc='Checking xml list for classnames'):
        filename = os.path.basename(xml_file)

        xmldoc = minidom.parse(xml_file)
        root = xmldoc.getElementsByTagName('Pages')
        pages = xmldoc.getElementsByTagName('Page')
        # Classnames for ALL pages in each file
        for page in pages:
            nodes = page.getElementsByTagName('Node')

            for node in nodes:
                node_classname = node.getElementsByTagName('ClassName')[0]
                node_classname_str = node_classname.firstChild.data
                if node_classname_str not in classnames_files.keys():
                    classnames_files[node_classname_str] = [filename]
                elif filename not in classnames_files[node_classname_str]:
                    classnames_files[node_classname_str].append(filename)
    with open(EXPORT_FILE, 'w') as outfile:
        json.dump(classnames_files, outfile, indent=4, sort_keys=True)


    # For each classname, add the current file if not existing
    # "noteheadBlack": [file1.xml, file2.xml]
    # Save all in json
if __name__ == '__main__':
    main()