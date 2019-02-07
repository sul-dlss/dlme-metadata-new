import os
from lxml import etree

# Parsing into one record per file

files = ['kitapvehat/data/kitapvehat.xml']

for file in files:
    tree = etree.parse(file)
    for bad in tree.xpath("//ListRecords/record/header[@status=\'deleted\']"):
        bad.getparent().remove(bad)
    # records = tree.findall("record")
    # file_count = 1
    # for record in records:
    #     if not record.get("status") = "deleted":
    #         next_file = open('{}/data/{}-{}.xml'.format(item, item, file_count), 'w')
    #         next_file.write(etree.tostring(record, encoding='unicode', pretty_print=True))
    #         file_count += 1
    #         next_file.close()
