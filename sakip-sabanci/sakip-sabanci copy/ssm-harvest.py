import errno
import os
from lxml import etree
from sickle import Sickle
from sickle.iterator import OAIResponseIterator

def to_str(bytes_or_str):
    '''Takes bytes or string and returns string'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

sickle = Sickle('http://cdm21044.contentdm.oclc.org/oai/oai.php', iterator=OAIResponseIterator)

sets = ['Kitapvehat', 'ResimKlksyn', 'emirgan', 'abidindino']

for item in sets:
    records = sickle.ListRecords(metadataPrefix='oai_dc', set=item)
    file_name = '{}/data/{}.xml'.format(item, item)
    if not os.path.exists(os.path.dirname(file_name)):
        try:
            os.makedirs(os.path.dirname(file_name))
        except OSError as exc: 
            if exc.errno != errno.EEXIST:
                raise
    
    with open(file_name, 'w') as f:
        for page in records:
            f.write(to_str(records.next().raw.encode('utf8')))
    
    f.close()

# # Parsing into one record per file

# files = []
# for item in set:
#     files.append('{}/data/{}.xml'.format(item, item))

# for file in files:
#     tree = etree.parse(file)
#     records = etree.Xpath("records/record") 
#     records = tree.findall("record") 
#     file_count = 1
#     for record in records:
#         if not record.get("status") = "deleted":
#             next_file = open('{}/data/{}-{}.xml'.format(item, item, file_count), 'w')
#             next_file.write(etree.tostring(record, encoding='unicode', pretty_print=True))
#             file_count += 1
#             next_file.close()
#     #os.remove(file)