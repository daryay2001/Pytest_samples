# Implement provided methods. You need to convert the class instance to JSON or XML.
# When the user provides the command json to cli, the program should call convert_to_json,
# when providing xml to cli program should convert the class instance to xml string.
# And print it, or even better write it to a separate file.
#
# You can use third parties libraries for this. If you use such a library please add it to requirenment.txt

import json
import xml.etree.ElementTree as ET
import argparse


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        human_data = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "birth_year": self.birth_year
        }
        return json.dumps(human_data)

    def convert_to_xml(self):
        root = ET.Element("human")
        name_elem = ET.SubElement(root, "name")
        name_elem.text = self.name
        age_elem = ET.SubElement(root, "age")
        age_elem.text = str(self.age)
        gender_elem = ET.SubElement(root, "gender")
        gender_elem.text = self.gender
        birth_year_elem = ET.SubElement(root, "birth_year")
        birth_year_elem.text = str(self.birth_year)

        xml_string = ET.tostring(root, encoding="utf-8", method="xml")
        return xml_string.decode("utf-8")


if __name__ == '__main__':

    try:
        my_human = Human("Tom Riddle", 16, "Male", 1947)

        parser = argparse.ArgumentParser(description="Convert Human elem to json or xml.")
        parser.add_argument("output_format", choices=["json", "xml"],
                            help="Choose output format (json or xml)")
        parser.add_argument("output_file", help="Give name to the output file")
        args = parser.parse_args()

        if args.output_format == "json":
            json_data = my_human.convert_to_json()
            with open(args.output_file, "w") as json_f:
                json_f.write(json_data)
            print(f"Data was saved to {args.output_file}")
        elif args.output_format == "xml":
            xml_data = my_human.convert_to_xml()
            with open(args.output_file, "w") as xml_f:
                xml_f.write(xml_data)
            print(f"Data was saved to {args.output_file}")
        else:
            raise TypeError("Invalid output format. Please choose 'json' or 'xml'.")
    except Exception as error:
        print(error)

# Щоб обрати формат виводу json: python human_converter.py json output.json

# Щоб обрати формат виводу xml python human_converter.py xml output.xml
