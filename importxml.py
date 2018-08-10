from xml.etree import ElementTree as ET

tree = ET.parse('data-text.xml')
root = tree.getroot()
data = root.find('Data')

all_data = []

for observation in data:
    record={}
    for item in observation:
        # Now,WHO data has Comment tag without attribute
        if item.keys() == []:
            continue

        # To take advantage of such implementations, use the dictionary methods below whenever possible.(about attrib)
        lookup_key = item.keys()[0]

        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.get('Numeric')
        else:
            rec_key = item.get(lookup_key)
            rec_value = item.get('Code')
        
        record[rec_key] = rec_value
    
    all_data.append(record)

import pprint
pprint.pprint(all_data)
