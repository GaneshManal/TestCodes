'''
module: sample program to read data from file and create valid json data
author: ganeshm
'''
import json


def extract_data_from_content(data):
    '''
    details: read the text and generate json data
    input: lines of text
    output: equivalent json data
    '''
    all_lines = data.split('\n')
    json_data = {}
    for line_no, line_content in enumerate(all_lines):
        line_data = line_content.strip().split()
        json_data[line_no] = {}
        for item in line_data:
            key, val = item.split(":")
            json_data[line_no].update({key: val})
    return json_data


if __name__ == "__main__":
    # read the data from file
    DATA_CONTENT = '''first_name:ganesh last_name:manal
    address:pune
    pin:411057'''
    txt_to_json = extract_data_from_content(DATA_CONTENT)
    print(json.dumps(txt_to_json))
